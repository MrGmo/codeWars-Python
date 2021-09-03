class Block:
  def __init__(self, dim): self.w, self.l, self.h = dim
  def get_width(self): return self.w
  def get_length(self): return self.l
  def get_height(self): return self.h
  def get_volume(self): return self.get_width() * self.get_length() * self.get_height()
  def get_surface_area(self):
    return 2 * self.get_width() * self.get_length() + 2 * self.get_width() * self.get_height() + 2 * self.get_length() * self.get_height()