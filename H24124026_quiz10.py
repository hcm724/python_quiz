import random
import curses
import time

# 初始化視窗
screen = curses.initscr()
curses.curs_set(0)  # 隱藏游標
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)  # 啟用鍵盤輸入
window.timeout(100)  # 設置輸入延遲

# 初始化顏色
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

# 初始化蛇和食物
snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [(snake_y, x) for x in range(snake_x, snake_x + 3)]
food = []
special_food = []
obstacles = []

# 生成障礙物
obstacle_count = int(screen_height * screen_width * 0.05)
for _ in range(obstacle_count):
    while True:
        obstacle_x = random.randint(0, screen_width - 1)
        obstacle_y = random.randint(0, screen_height - 1)
        if (obstacle_y, obstacle_x) not in snake and (obstacle_y, obstacle_x) not in obstacles:
            obstacle_length = random.randint(5, 10)
            obstacle_orientation = random.choice(['horizontal', 'vertical'])
            if obstacle_orientation == 'horizontal':
                if obstacle_x + obstacle_length < screen_width:
                    obstacle = [(obstacle_y, obstacle_x + i) for i in range(obstacle_length)]
                    obstacles.extend(obstacle)
                    break
            else:
                if obstacle_y + obstacle_length < screen_height:
                    obstacle = [(obstacle_y + i, obstacle_x) for i in range(obstacle_length)]
                    obstacles.extend(obstacle)
                    break

# 生成食物
def generate_food():
    while True:
        food_x = random.randint(0, screen_width - 1)
        food_y = random.randint(0, screen_height - 1)
        if (food_y, food_x) not in snake and (food_y, food_x) not in obstacles:
            food.append((food_y, food_x))
            break

def generate_special_food():
    while True:
        food_x = random.randint(0, screen_width - 1)
        food_y = random.randint(0, screen_height - 1)
        if (food_y, food_x) not in snake and (food_y, food_x) not in obstacles and (food_y, food_x) not in food:
            special_food.append((food_y, food_x))
            break

generate_food()
generate_special_food()

# 初始化遊戲狀態
score = 0
special_score = 0
key = curses.KEY_RIGHT
paused = False
game_over = False

# 遊戲循環
while not game_over:
    window.clear()
    next_key = window.getch()

    # 處理暫停
    if next_key == ord(' '):
        paused = not paused

    # 處理移動
    if not paused:
        new_head = (snake[0][0] + (key == curses.KEY_DOWN and 1) + (key == curses.KEY_UP and -1),
                    snake[0][1] + (key == curses.KEY_LEFT and -1) + (key == curses.KEY_RIGHT and 1))

        # 處理蛇繞場
        new_head = (new_head[0] % screen_height, new_head[1] % screen_width)

        # 檢查碰撞
        if new_head in snake or new_head in obstacles:
            game_over = True
        else:
            snake.insert(0, new_head)

            # 處理食物
            if new_head in food:
                score += 1
                food.remove(new_head)
                generate_food()
            elif new_head in special_food:
                special_score += 1
                special_food.remove(new_head)
                generate_special_food()
            else:
                snake.pop()

            # 更新鍵盤輸入
            key = next_key

    # 繪製遊戲元素
    for y in range(screen_height):
        for x in range(screen_width):
            if (y, x) in snake:
                window.addch(y, x, '#', curses.color_pair(1))
            elif (y, x) in food:
                window.addch(y, x, 'π', curses.color_pair(2))
            elif (y, x) in special_food:
                window.addch(y, x, 'X', curses.color_pair(3))
            elif (y, x) in obstacles:
                window.addch(y, x, '█', curses.color_pair(4))

    # 顯示分數
    score_text = f"Score: {score}"
    special_score_text = f"Special Score: {special_score}"
    window.addstr(0, 0, score_text)
    window.addstr(1, 0, special_score_text)

    # 檢查遊戲結束
    if game_over:
        window.addstr(screen_height // 2, screen_width // 2 - 5, "Game Over")
        window.addstr(screen_height // 2 + 1, screen_width // 2 - 10, f"Normal Food Eaten: {score}")
        window.addstr(screen_height // 2 + 2, screen_width // 2 - 12, f"Special Food Eaten: {special_score}")
        window.getch()
        break

    window.refresh()
    time.sleep(0.1)  # 調整遊戲速度

# 清理視窗
curses.endwin()