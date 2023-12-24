import sys,os
from pypinyin import lazy_pinyin

sys.path.append(os.path.split(sys.path[0])[0])
print(os.path.split(sys.path[0])[0])

from LLM_dialogue import LLM_api
from LLM_dialogue import multiple_Requests
from LLM_dialogue import intention_Recognition
from voice_express import text2voice
from persuading import *

# 模型初始化
memory = multiple_Requests.init_memory()
my_model = LLM_api.unitModel()

# 页面初始化
all_sprites = pygame.sprite.Group()
text = Text()
dz = Dingzhen()
all_sprites.add(text)
all_sprites.add(dz)
pygame.mixer.music.play(-1)

text_box = TextBox(600, 40, WIDTH/2-300, HEIGHT-120)
# Add the input box to the sprite group
input_box = Input()
all_sprites.add(input_box)

def convert_pinyin_to_hanzi(pinyin_text):
    # 这里的转换非常简单，不考虑多音字或词组
    return ''.join(lazy_pinyin(pinyin_text))

show_init = True
running = True
#loop
while running:
    if show_init:
        draw_init()
        show_init = False

    clock.tick(FPS)
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            text_box.safe_key_down(event)
            if event.key == pygame.K_RETURN:
                user_Question = text_box.text
                converted_text = convert_pinyin_to_hanzi(user_Question)
                print(user_Question)
                multiple_Requests.question(memory=memory, quest=user_Question)
                if user_Question == '退出':
                    break
                else:
                    llm_Answer = my_model.respond(model_name='ERNIE-Bot', input=memory)
                    text2voice(llm_Answer)
                    multiple_Requests.answer(memory=memory, ans=llm_Answer)
                    text.result = llm_Answer
                    print(llm_Answer)
                    play_latest_sound()
                    judge = intention_Recognition.recognition(llm_Answer)

                    if intention_Recognition.contains_word_no('文本：' + judge):
                        input_box.clear_text()  # 清空输入框
                        continue
                    else:
                        break
            elif input_box.active:
                if event.key == pygame.K_BACKSPACE:
                    input_box.backspace()
                else:
                    input_box.add_character(event.unicode)

    #update
    #Execute the update function for each object in this group
    all_sprites.update()

    #display
    screen.fill(BLACK)
    screen.blit(background_img, (0,0))
    all_sprites.draw(screen)
    text_box.draw(screen)  # 绘制 TextBox
    #refresh
    pygame.display.update()

pygame.quit()