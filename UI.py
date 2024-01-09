class UI:
	def __init__(self):
		pass

	def items_draw(self, values):
		y = 64  # вывод снаряжения
		for item in player.inventory.values():
			if item:
				window.blit(item.image, (width - 64, y - 64))
				window.blit(font.render(str(item.stat), True, 'white'), (1280 - 80, y - 24))
			y += 64