from threading import RLock
from chaser import io as gpio

IN1_PIN = 4
IN2_PIN = 17

IN3_PIN = 24
IN4_PIN = 25

LEFT_KEY = u'37'
UP_KEY = u'38'
RIGHT_KEY = u'39'
DOWN_KEY = u'40'

# lock for the controller
io_lock = RLock()

gpio.setmode(gpio.BCM)

CONTROLLER_STATES = {
    'stopped': 'stopped',
    UP_KEY: 'forward',
    LEFT_KEY: 'left',
    RIGHT_KEY: 'right',
    DOWN_KEY: 'backwards'
}

_STATE = CONTROLLER_STATES.get('stopped')


class MotorInputError(Exception):
    pass


class MotorController(object):
    """Motor controller for the flask container.
    left - configures the io pins for a left turn.
        calling subsequent left turns will center the wheels
    right - configures the io pins for a right turn.
        calling subsequent right turns will center the wheels
    forward - configures the io pins for a forward.
        calling subsequent forward calls will stop the car
    reverse - configures the io pins for a reverse.
        calling subsequent reverse calls will stop the car
    """
    def __init__(self):
        with io_lock:
            gpio.setup(IN1_PIN, gpio.OUT)
            gpio.setup(IN2_PIN, gpio.OUT)
            gpio.setup(IN3_PIN, gpio.OUT)
            gpio.setup(IN4_PIN, gpio.OUT)

            self.progress_keys = set()
            self.turn_keys = set()

    @property
    def state(self):
        with io_lock:
            global _STATE
            return _STATE

    def shut_down(self):
        with io_lock:
            self.__stop(IN1_PIN, IN2_PIN)
            self.__stop(IN3_PIN, IN4_PIN)

    def left(self):
        self.__call_or_stop(
            IN3_PIN,
            IN4_PIN,
            LEFT_KEY,
            RIGHT_KEY,
            self.turn_keys
        )

    def right(self):
        self.__call_or_stop(
            IN4_PIN,
            IN3_PIN,
            RIGHT_KEY,
            LEFT_KEY,
            self.turn_keys
        )

    def forward(self):
        self.__call_or_stop(
            IN1_PIN,
            IN2_PIN,
            UP_KEY,
            DOWN_KEY,
            self.progress_keys
        )

    def reverse(self):
        self.__call_or_stop(
            IN2_PIN,
            IN1_PIN,
            DOWN_KEY,
            UP_KEY,
            self.progress_keys
        )

    def __run(self, on_pin, off_pin):
        with io_lock:
            gpio.output(on_pin, True)
            gpio.output(off_pin, False)

    def __stop(self, pin_one, pin_two):
        with io_lock:
            gpio.output(pin_one, False)
            gpio.output(pin_two, False)

    def __call_or_stop(self, in1_pin, in2_pin, key, reverse_key, key_store):
        with io_lock:
            global _STATE
            if key in key_store:
                key_store.remove(key)
                self.__stop(in1_pin, in2_pin)
                _STATE = CONTROLLER_STATES.get('stopped')
            else:
                key_store.add(key)
                try:
                    key_store.remove(reverse_key)
                except KeyError:
                    pass

                self.__run(in1_pin, in2_pin)
                _STATE = CONTROLLER_STATES[key]

    def motor(self, key):
        """
        :param key: One of the following keys [u'37', u'38' u'39' u'40']
        If its any other parameter it will be ignored.
        """
        if key is UP_KEY:
            self.forward()
        elif key == DOWN_KEY:
            self.reverse()
        elif key == LEFT_KEY:
            self.left()
        elif key == RIGHT_KEY:
            self.right()
        else:
            raise MotorInputError("Not supported input")
