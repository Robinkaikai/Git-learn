class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, wide):
        self._width = wide

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,high):
        self._height = high

    @property
    def resolution(self):
        return self._width * self._height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
