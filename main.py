import pygame


class Circle:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius


class Button():

    def __init__(self, text='OK', pos=(0, 0), size=(100, 50), command=None):
        font = pygame.font.SysFont(None, 35)

        self.text = text
        self.rect = pygame.Rect((0, 0), size)

        self.image_normal = pygame.Surface(size)
        self.image_normal.fill(WHITE)
        txt_image = font.render(self.text, True, BLACK)
        txt_rect = txt_image.get_rect(center=self.rect.center)
        self.image_normal.blit(txt_image, txt_rect)

        self.image_hover = pygame.Surface(size)
        self.image_hover.fill(RED)
        txt_image = font.render(self.text, True, WHITE)
        txt_rect = txt_image.get_rect(center=self.rect.center)
        self.image_hover.blit(txt_image, txt_rect)

        self.rect.topleft = pos

        self.hover = False

        if command:
            self.command = command

    def draw(self, screen):
        if self.hover:
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image_normal, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)

        if self.hover and self.command:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.command()

    def command(self):
        print("Click")


class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_collision(self, circle):
        circle_rect = pygame.Rect(circle.x - circle.radius, circle.y - circle.radius, circle.radius * 2, circle.radius * 2)
        return self.rect.colliderect(circle_rect)


def Black1():
    circles1.append(Circle(150, 350, BLACK, 22))


def White1():
    circles2.append(Circle(200, 350, WHITE, 22))


def Pink1():
    circles3.append(Circle(250, 350, PINK, 22))


def Blue1():
    circles4.append(Circle(300, 350, BLUE, 22))


def Jade1():
    circles5.append(Circle(350, 350, GREEN, 22))


def Purple1():
    circles6.append(Circle(400, 350, PURPLE, 22))


def Grey1():
    circles7.append(Circle(450, 350, GREY, 10))


def DeleteAll():
    circles1.clear()
    circles2.clear()
    circles3.clear()
    circles4.clear()
    circles5.clear()
    circles6.clear()
    circles7.clear()


def TakeScreenshot():
    global screenshot_count 
    filename = f"screenshot_{screenshot_count}.png" 
    pygame.image.save(screen, filename) 
    screenshot_count += 1


pygame.init()

screenshot_count = 1

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oregame")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 168, 107)
RED = (255, 0, 0)
BLUE = (173, 216, 255)
PINK = (255, 192, 203)
GREY = (128, 128, 128)
PURPLE = (153, 50, 204)

button1 = Button(text="Black", pos=(2, 2), size=(100, 50), command=Black1)
button2 = Button(text="White", pos=(112, 2), size=(100, 50), command=White1)
button3 = Button(text="Pink", pos=(222, 2), size=(100, 50), command=Pink1)
button4 = Button(text="Blue", pos=(332, 2), size=(100, 50), command=Blue1)
button5 = Button(text="Jade", pos=(442, 2), size=(100, 50), command=Jade1)
button6 = Button(text="Purple", pos=(552, 2), size=(100, 50), command=Purple1)
button7 = Button(text="Separ.", pos=(662, 2), size=(100, 50), command=Grey1)
delete_all_button = Button(text="Clear", pos=(662, 540), size=(100, 50), command=DeleteAll)
screenshot_button = Button(text="Screenshot", pos=(502, 540), size=(140, 50), command=TakeScreenshot)

circles1 = []
circles2 = []
circles3 = []
circles4 = []
circles5 = []
circles6 = []
circles7 = []

square = Square(0, SCREEN_HEIGHT - 50, 50, GREY)

active_circle = None
active_circle_offset = (0, 0)

run = True
while run:
    screen.fill(RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        button1.handle_event(event)
        button2.handle_event(event)
        button3.handle_event(event)
        button4.handle_event(event)
        button5.handle_event(event)
        button6.handle_event(event)
        button7.handle_event(event)
        delete_all_button.handle_event(event)
        screenshot_button.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, circle in enumerate(circles1 + circles2 + circles3 + circles4 + circles5 + circles6 + circles7):
                    dx = circle.x - event.pos[0]
                    dy = circle.y - event.pos[1]
                    distance = dx ** 2 + dy ** 2
                    if distance <= circle.radius ** 2:
                        active_circle = circle
                        active_circle_offset = (dx, dy)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_circle = None

        if event.type == pygame.MOUSEMOTION:
            if active_circle is not None:
                active_circle.x = event.pos[0] + active_circle_offset[0]
                active_circle.y = event.pos[1] + active_circle_offset[1]

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)
    button6.draw(screen)
    button7.draw(screen)
    delete_all_button.draw(screen)
    screenshot_button.draw(screen)
    square.draw(screen)

    for circle in circles1 + circles2 + circles3 + circles4 + circles5 + circles6 + circles7:
        pygame.draw.circle(screen, circle.color,
                           (circle.x, circle.y), circle.radius)
        if square.check_collision(circle):
            try:
                circles1.remove(circle)
            except ValueError:
                pass
            try:
                circles2.remove(circle)
            except ValueError:
                pass
            try:
                circles3.remove(circle)
            except ValueError:
                pass
            try:
                circles4.remove(circle)
            except ValueError:
                pass
            try:
                circles5.remove(circle)
            except ValueError:
                pass
            try:
                circles6.remove(circle)
            except ValueError:
                pass
            try:
                circles7.remove(circle)
            except ValueError:
                pass

    pygame.display.update()

pygame.quit()
