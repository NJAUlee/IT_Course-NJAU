import sys,os

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

# Add the input box to the sprite group
input_box = Input()
all_sprites.add(input_box)

running = True
#loop
while running:
    clock.tick(FPS)
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                user_Question = input_box.text
                print(user_Question)
                multiple_Requests.question(memory=memory, quest=user_Question)
                if user_Question == '退出':
                    break
                else:
                    llm_Answer = my_model.respond(model_name='ERNIE-Bot', input=memory)
                    #text2voice(llm_Answer)
                    multiple_Requests.answer(memory=memory, ans=llm_Answer)
                    text.result = llm_Answer
                    print(llm_Answer)
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
    #refresh
    pygame.display.update()

pygame.quit()