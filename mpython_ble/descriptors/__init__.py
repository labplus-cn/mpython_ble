# The MIT License (MIT)

# Copyright (c) 2020, Tangliufeng for labplus Industries

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from bluetooth import FLAG_NOTIFY, FLAG_READ, FLAG_WRITE


class Descriptor(object):
    def __init__(self, uuid, properties='-r'):
        self.uuid = uuid
        self.properties = (True if 'r' in properties else False,
                           True if 'w' in properties else False)
        self.flags = (0x01 if self.properties[0] else 0x00) | (0x02 if self.properties[1] else 0x03)
        self.value_handle = None

    def __repr__(self):
        properties_ = '-'
        if self.properties[0]:
            properties_ += 'r'
        if self.properties[1]:
            properties_ += 'w'
        return "<{} {}, '{}'>" .format(self.__class__.__name__, self.uuid, properties_)

    @property
    def definition(self):
        return (self.uuid, self.flags)
