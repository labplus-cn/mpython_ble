:py:mod:`mpython_ble.hidcode`
=================================

HID设备(Human Interface Devices)键值常量定义


.. Hint::

   如果你的可用内存不多,不建议你使用 hidcode 模块。你可按需,自行定义常量,减少不必要的内存浪费。


KeyboardCode
--------------

鼠标常量

.. py:class:: KeyboardCode()

   .. py:attribute:: KeyboardCode.LEFT = 1
   .. py:attribute:: KeyboardCode.MIDDLE = 2
   .. py:attribute:: KeyboardCode.RIGHT = 4

KeyboardCode
--------------

.. py:class:: KeyboardCode()

   .. py:attribute:: KeyboardCode.A = 0x04

   ``a`` and ``A``

   .. py:attribute:: KeyboardCode.B = 0x05

   ``b`` and ``B``

   .. py:attribute:: KeyboardCode.C = 0x06

   ``c`` and ``C``

   .. py:attribute:: KeyboardCode.D = 0x07

   ``d`` and ``D``

   .. py:attribute:: KeyboardCode.E = 0x08

   ``e`` and ``E``

   .. py:attribute:: KeyboardCode.F = 0x09

   ``f`` and ``F``

   .. py:attribute:: KeyboardCode.G = 0x0A

   ``g`` and ``G``

   .. py:attribute:: KeyboardCode.H = 0x0B

   ``h`` and ``H``

   .. py:attribute:: KeyboardCode.I = 0x0C

   ``i`` and ``I``

   .. py:attribute:: KeyboardCode.J = 0x0D

   ``j`` and ``J``

   .. py:attribute:: KeyboardCode.K = 0x0E

   ``k`` and ``K``

   .. py:attribute:: KeyboardCode.L = 0x0F

   ``l`` and ``L``

   .. py:attribute:: KeyboardCode.M = 0x10

   ``m`` and ``M``

   .. py:attribute:: KeyboardCode.N = 0x11

   ``n`` and ``N``

   .. py:attribute:: KeyboardCode.O = 0x12

   ``o`` and ``O``

   .. py:attribute:: KeyboardCode.P = 0x13

   ``p`` and ``P``

   .. py:attribute:: KeyboardCode.Q = 0x14

   ``q`` and ``Q``

   .. py:attribute:: KeyboardCode.R = 0x15

   ``r`` and ``R``

   .. py:attribute:: KeyboardCode.S = 0x16

   ``s`` and ``S``

   .. py:attribute:: KeyboardCode.T = 0x17

   ``t`` and ``T``

   .. py:attribute:: KeyboardCode.U = 0x18

   ``u`` and ``U``

   .. py:attribute:: KeyboardCode.V = 0x19

   ``v`` and ``V``

   .. py:attribute:: KeyboardCode.W = 0x1A

   ``w`` and ``W``

   .. py:attribute:: KeyboardCode.S = 0x1B

   ``x`` and ``X``

   .. py:attribute:: KeyboardCode.Y = 0x1C

   ``y`` and ``Y``

   .. py:attribute:: KeyboardCode.Z = 0x1D

   ``z`` and ``Z``

   .. py:attribute:: KeyboardCode.ONE = 0x1E

   ``1`` and ``!``

   .. py:attribute:: KeyboardCode.TWO = 0x1F

   ``2`` and ``@``

   .. py:attribute:: KeyboardCode.THREE = 0x20

   ``3`` and ``#``

   .. py:attribute:: KeyboardCode.FOUR = 0x21

   ``4`` and ``$``

   .. py:attribute:: KeyboardCode.FIVE = 0x22

   ``5`` and ``%``

   .. py:attribute:: KeyboardCode.SIX = 0x23

   ``6`` and ``^``

   .. py:attribute:: KeyboardCode.SEVEN = 0x24

   ``7`` and ``&``

   .. py:attribute:: KeyboardCode.EIGHT = 0x25

   ``8`` and ``*``

   .. py:attribute:: KeyboardCode.NINE = 0x26

   ``9`` and ``(``

   .. py:attribute:: KeyboardCode.ZERO = 0x27

   ``0`` and ``)``

   .. py:attribute:: KeyboardCode.ENTER = 0x28

   Enter

   .. py:attribute:: KeyboardCode.ESCAPE = 0x29

   Escape

   .. py:attribute:: KeyboardCode.BACKSPACE = 0x2A

   Delete backward (Backspace)
   
   .. py:attribute:: KeyboardCode.TAB = 0x2B

   Tab and Backtab

   .. py:attribute:: KeyboardCode.SPACE = 0x2C

   Space

   .. py:attribute:: KeyboardCode.MINUS = 0x2D

   ``-` and ``_``

   .. py:attribute:: KeyboardCode.EQUALS = 0x2E

   ``=` and ``+``

   .. py:attribute:: KeyboardCode.LEFT_BRACKET = 0x2F

   ``[`` and ``{``

   .. py:attribute:: KeyboardCode.RIGHT_BRACKET = 0x30

   ``]`` and ``}``

   .. py:attribute:: KeyboardCode.BACKSLASH = 0x31

   ``\`` and ``|``

   .. py:attribute:: KeyboardCode.POUND = 0x32

   ``#`` and ``~``

   .. py:attribute:: KeyboardCode.SEMICOLON = 0x33

   ``;`` and ``:``

   .. py:attribute:: KeyboardCode.QUOTE = 0x34

   ``'`` and ``"``

   .. py:attribute:: KeyboardCode.GRAVE_ACCENT = 0x35

   :literal:`\`` and ``~``

   .. py:attribute:: KeyboardCode.COMMA = 0x36

   ``,`` and ``<``

   .. py:attribute:: KeyboardCode.PERIOD = 0x37

   ``.`` and ``>``

   .. py:attribute:: KeyboardCode.FORWARD_SLASH = 0x38

   ``/`` and ``?``

   .. py:attribute:: KeyboardCode.CAPS_LOCK = 0x39

   Caps Lock

   .. py:attribute:: KeyboardCode.F1 = 0x3A

   Function key F1

   .. py:attribute:: KeyboardCode.F2 = 0x3B

   Function key F2

   .. py:attribute:: KeyboardCode.F3 = 0x3C

   Function key F3

   .. py:attribute:: KeyboardCode.F4 = 0x3D

   Function key F4

   .. py:attribute:: KeyboardCode.F5 = 0x3E

   Function key F5

   .. py:attribute:: KeyboardCode.F6 = 0x3F

   Function key F6

   .. py:attribute:: KeyboardCode.F7 = 0x40

   Function key F7

   .. py:attribute:: KeyboardCode.F8 = 0x41

   Function key F8

   .. py:attribute:: KeyboardCode.F9 = 0x42

   Function key F9

   .. py:attribute:: KeyboardCode.F10 = 0x43

   Function key F10

   .. py:attribute:: KeyboardCode.F11 = 0x44

   Function key F11

   .. py:attribute:: KeyboardCode.F12 = 0x45

   Function key F12

   .. py:attribute:: KeyboardCode.PRINT_SCREEN = 0x46

   Print Screen (SysRq)

   .. py:attribute:: KeyboardCode.SCROLL_LOCK = 0x47

   Scroll Lock

   .. py:attribute:: KeyboardCode.PAUSE = 0x48

   Pause (Break)

   .. py:attribute:: KeyboardCode.INSERT = 0x49

   Insert

   .. py:attribute:: KeyboardCode.HOME = 0x4A

   Home

   .. py:attribute:: KeyboardCode.PAGE_UP = 0x4B

   Go back one page

   .. py:attribute:: KeyboardCode.DELETE = 0x4C

   Delete forward

   .. py:attribute:: KeyboardCode.END = 0x4D

   End

   .. py:attribute:: KeyboardCode.PAGE_DOWN = 0x4E

   Go forward one page

   .. py:attribute:: KeyboardCode.RIGHT_ARROW = 0x4F

   Move the cursor right

   .. py:attribute:: KeyboardCode.LEFT_ARROW = 0x50

   Move the cursor left

   .. py:attribute:: KeyboardCode.DOWN_ARROW = 0x51

   Move the cursor down

   .. py:attribute:: KeyboardCode.UP_ARROW = 0x52

   Move the cursor up

   .. py:attribute:: KeyboardCode.KEYPAD_NUMLOCK = 0x53

   Num Lock

   .. py:attribute:: KeyboardCode.KEYPAD_FORWARD_SLASH = 0x54

   Keypad ``/``

   .. py:attribute:: KeyboardCode.KEYPAD_ASTERISK = 0x55

   Keypad ``*``

   .. py:attribute:: KeyboardCode.KEYPAD_MINUS = 0x56

   Keyapd ``-``

   .. py:attribute:: KeyboardCode.KEYPAD_PLUS = 0x57

   Keypad ``+``

   .. py:attribute:: KeyboardCode.KEYPAD_ENTER = 0x58

   Keypad Enter

   .. py:attribute:: KeyboardCode.KEYPAD_ONE = 0x59

   Keypad ``1`` and End

   .. py:attribute:: KeyboardCode.KEYPAD_TWO = 0x5A

   Keypad ``2`` and Down Arrow

   .. py:attribute:: KeyboardCode.KEYPAD_THREE = 0x5B

   Keypad ``3`` and PgDn

   .. py:attribute:: KeyboardCode.KEYPAD_FOUR = 0x5C

   Keypad ``4`` and Left Arrow

   .. py:attribute:: KeyboardCode.KEYPAD_FIVE = 0x5D

   Keypad ``5``

   .. py:attribute:: KeyboardCode.KEYPAD_SIX = 0x5E

   Keypad ``6`` and Right Arrow

   .. py:attribute:: KeyboardCode.KEYPAD_SEVEN = 0x5F

   Keypad ``7`` and Home

   .. py:attribute:: KeyboardCode.KEYPAD_EIGHT = 0x60

   Keypad ``8`` and Up Arrow

   .. py:attribute:: KeyboardCode.KEYPAD_NINE = 0x61

   Keypad ``9`` and PgUp

   .. py:attribute:: KeyboardCode.KEYPAD_ZERO = 0x62

   Keypad ``0`` and Ins

   .. py:attribute:: KeyboardCode.KEYPAD_PERIOD = 0x63

   Keypad ``.`` and Del

   .. py:attribute:: KeyboardCode.KEYPAD_BACKSLASH = 0x64

   Keypad ``\\`` and ``|`` 

   .. py:attribute:: KeyboardCode.KEYPAD_EQUALS = 0x67

   Keypad ``=`` (Mac)

   .. py:attribute:: KeyboardCode.F13 = 0x68

   Function key F13 (Mac)

   .. py:attribute:: KeyboardCode.F14 = 0x69

   Function key F14 (Mac)

   .. py:attribute:: KeyboardCode.F15 = 0x6A

   Function key F15 (Mac)

   .. py:attribute:: KeyboardCode.F16 = 0x6B

   Function key F16 (Mac)

   .. py:attribute:: KeyboardCode.F17 = 0x6C

   Function key F17 (Mac)

   .. py:attribute:: KeyboardCode.F18 = 0x6D

   Function key F18 (Mac)

   .. py:attribute:: KeyboardCode.F19 = 0x6E

   Function key F19 (Mac)

   .. py:attribute:: KeyboardCode.LEFT_CONTROL = 0xE0

   Control modifier left 

   .. py:attribute:: KeyboardCode.CONTROL = LEFT_CONTROL

   Control modifier 

   .. py:attribute:: KeyboardCode.LEFT_SHIFT = 0xE1

   Shift modifier left 

   .. py:attribute:: KeyboardCode.SHIFT = LEFT_SHIFT

   Shift modifier

   .. py:attribute:: KeyboardCode.LEFT_ALT = 0xE2

   Alt modifier left 

   .. py:attribute:: KeyboardCode.ALT = LEFT_ALT

   Alt modifier

   .. py:attribute:: KeyboardCode.OPTION = ALT

   Labeled as Option on some Mac keyboards

   .. py:attribute:: KeyboardCode.LEFT_GUI = 0xE3

   GUI modifier left 

   .. py:attribute:: KeyboardCode.RIGHT_CONTROL = 0xE4

   Control modifier right

   .. py:attribute:: KeyboardCode.RIGHT_SHIFT = 0xE5
   .. py:attribute:: KeyboardCode.RIGHT_ALT = 0xE6
   .. py:attribute:: KeyboardCode.RIGHT_GUI = 0xE7



ConsumerCode
--------------

消费类常量

.. py:class:: ConsumerCode()

   .. py:attribute:: ConsumerCode.POWER = 0x30
   .. py:attribute:: ConsumerCode.CHANNEL_UP = 0X9C
   .. py:attribute:: ConsumerCode.CHANNEL_DOWN = 0X9D
   .. py:attribute:: ConsumerCode.RECORD = 0xB2
   .. py:attribute:: ConsumerCode.FAST_FORWARD = 0xB3
   .. py:attribute:: ConsumerCode.REWIND = 0xB4
   .. py:attribute:: ConsumerCode.SCAN_NEXT_TRACK = 0xB5
   .. py:attribute:: ConsumerCode.SCAN_PREVIOUS_TRACK = 0xB6
   .. py:attribute:: ConsumerCode.STOP = 0xB7
   .. py:attribute:: ConsumerCode.EJECT = 0xB8
   .. py:attribute:: ConsumerCode.PLAY_PAUSE = 0xCD
   .. py:attribute:: ConsumerCode.MUTE = 0xE2
   .. py:attribute:: ConsumerCode.VOLUME_DECREMENT = 0xEA
   .. py:attribute:: ConsumerCode.VOLUME_INCREMENT = 0xE9