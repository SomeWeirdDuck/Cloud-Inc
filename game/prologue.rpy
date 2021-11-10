init:
    $ prolog = 0

label prologue:

    scene clouds

    python:
        user_name = renpy.input("Введите имя персонажа: ")
        user_name = user_name.strip()
        me = user_name + "Ъ"
        if not user_name:
            pass

    scene black
    with dissolve
    scene clouds
    with dissolve

    n "Облака плывут так медленно, удивительно..."
    n "Уже не помню, когда я последний раз на них смотрел."
    n "Одно похоже на якорь, другое на кошку, третье..."
    n "Оно уже расплылось. {w}На что же оно было похоже? "
    n "А впрочем... {w}Не важно."
    n "Вижу, ты уже здесь. {w}Я надеюсь, что могу на тебя положиться..."
    n "И... {w}Да, удачи!"

    nvl clear

    scene hata
    with dissolve

    "Фух! Приснится же такое! Лучше б это был кошмар."
    "Сколько там время?"
    "10:12?! Чёрт!!!"
    "Нужно бежать, срочно!"
    "Даже рубашку погладить не успел!"
    me "Мам, пока! Я побежал!"
    mom "Удачи там! Люблю теб..."

    scene street
    with dissolve

    "Дверь захлопнулась, и вот я на улице, несусь к ближайшей остановке."
    "Интересно, а они попросят документы, диплом?"
    "Или может это жадная конторка? И ей нужны только деньги?"
    "Да нее... Бред!"
    "10:29, еле успел! Через минуту мой автобус!"
    "*Раздается плач*"
    "Э... Ээ... Кажется, кто-то плачет."
    window hide
    $ renpy.pause(0.5)
    menu:
        "Пойти на плач":
            jump kid_with_phone
        "Сесть в автобус":
            jump bus
label bus:

    "Да вообщем-то плевать!"
    "Я не для этого 19 лет проучился, чтобы променять карьеру на плач!"
    "Я захожу в распахнувшиеся передо мной автобусные двери и сажусь на свободное одинокое сиденье."
    "Так как делать особо нечего, я решил попялться в окно."
    "Пейзажи белых домов с цветущими клумбами, то и дело, проносились мимо меня."
    "Облако... Расплывается..."
    "Оно выглядело как... Те..."
    "Ой. Кажется, я задремал."
    "Черт, это моя остановка!"
    "Взяв вещи, я в спешке вышел из автобуса."

    jump office_entrance

label kid_with_phone:
    $ prolog += 1
    "Разве я мужчина, если не помогу в беде?"
    "Я разворачиваюсь и вижу плачущего мальчика, лет восьми."
    me "Что с тобой, дитя?"

    show kid1_crying
    with dissolve

    kid1 "Вы не видели мой телефон?"
    me "Как он выглядит?"
    kid1 "М-маленький, серый, с кнопками..."
    me "Хмм, давай поищем его."
    kid1 "С... Спасибо вам..."
    "Разве я мог отказать ребенку?"
    "А вдруг в этом телефоне контакты его родителей, и ему нужно позвонить?"
    "Спустя минуты три ходьбы вокруг остановки, мы нашли телефон."
    "Он лежал около припаркованной машины."
    "Ребенок, со слезами на глазах, поблагодарил меня и побежал."

    hide kid1_crying
    with easeoutright

    "Похоже, добираться теперь придется на такси."

    jump office_entrance

label office_entrance:

    scene Cloud_Building
    with dissolve

    "Офис Cloud inc., наконец-то я здесь!"
    "Такой красивый белый фасад... И эта надпись, ухх!"
    "Но не время его осматривать, я побежал к входным дверям, которые сами, словно ждали меня, распахнулись."
    "А там, внутри... Удобные мягкие диванчики, несколько лифтов, куча дверей и, конечно, оператор."
    op "Здравствуйте, я приветствую вас в Cloud.inc. Спасибо, что выбрали именно нас!"
    op "Ваш личный кабинет находится на 273-ем этаже."
    me "..."
    op "Что-то не так?"
    me "А собеседование? Подача доку-"
    op "Кхм... 273-ий этаж."
    me "..."
    "Как же... Что за?!"
    "Тут столько этажей?! О боже, нервы."
    "Та-ак, лифт."
    "После нажатия кнопки, двери лифта мгновенно распахнулись."
    "Неужели в нем никто не ехал, и он все это время был на первом этаже?"
    "Я зашел внутрь, двери сразу закрылись и голосовая система предложила мне выбрать этаж."
    me "273-ий!"
    "Ничего не произошло."
    me "273-ий! {w}273-ий этаж. {w}{cps=8.5}ЭТАЖ ДВЕСТИ СЕМЬДЕСЯТ ТРИ.{/cps}"
    "Двери неожиданно распахнулись."
    "Я увидел три двери."
    "«Каб. 273.1», «Каб. 273.2», «Каб. 273.3»."
    "Кажется, это действительно 273-ий этаж, до чего технологии дошли!"
    "Осталось понять одно - какой из кабинетов мой?"
    "Я решил выбрать центральный - «273.2»."
    "Дверь легко открылась, и я увидел свое новое рабочее место!"
    "Компьютерный стол, удобное кожаное кресло, микроволновка, холодильник и... кровать?!"
    "Я еще и спать тут могу?!"
    "Я кинул сумку с документами на кровать и подошел к столу, сел на кресло."
    "Кайф! Просто кайф! Еще и это огромное окно, правда, видно только облака."
    "Я увидел на столе записку и, логично, решил прочесть."

    n "{i}«Здравствуйте, мы рады, что вы решили выбрать Cloud inc. Прежде, чем вы начнете работать, вам нужно запомнить несколько правил:{/i}"
    n "{i}1. Не портите и не вскрывайте посылки.{/i}"
    n "{i}2. Не отвлекайте других работников.{/i}"
    n "{i}3. Не покидайте офис ни в какие дни, кроме воскресенья.{/i}"
    n "{i}Еду вы всегда можете заказать, позвонив по телефону (бесплатно).{/i}"
    n "{i}За хорошую работу вы будете получать надбавки и различные бонусы.{/i}"
    n "{i}Приятной работы в Cloud inc. <3».{/i}"
    nvl clear

    "Ни в какие дни, кроме воскресенья? Что?"
    "Хотя...Бесплатная еда и возможность обустроить комнату под себя… Думаю, Cloud Inc станет моим вторым домом."
    "Разве это не круто? Всю жизнь мечтал о том, чтобы тут работать."


    window hide
    play sound knock
    $renpy.pause(0.8)
    window show



    "А? Кто-то стучится в дверь, нужно открыть."
    me "Да, здрасьте."
    rab "Я из 272.2, передай это на 274.2 и попроси передать на 275.2."
    me "И… всё?"
    rab "Да."
    me "А почему я не могу сразу передать на 275.2?"
    rab "Не отвлекай других работников."
    "Работник развернулся и зашел в лифт, а я в ступоре смотрел на посылку."
    "Картонная коробка, небольшая, с кучей текста и красочным логотипом Cloud Inc."
    "Интересно здесь все такие строгие или мне просто “повезло”?"
    "Так или иначе, работа есть работа. "
    "Я переступил порог своего кабинета, закрыл дверь и вызвал лифт, что через секунду уже открылся."
    me "274-ый этаж."
    "Двери закрылись и тут же стали открываться."
    "Передо мной те же 3 двери, что и на моем этаже, но теперь на них написано «274.1», «274.2» и «274.3». Я снова иду к центральной."
    "После короткого стука мне открывает девушка. По виду моя ровесница."
    me "Здрасте, вот посылка, её надо…"
    ht "Да, я уже знаю. Ты новенький?"
    me "Д-да. Сегодня мой первый день."
    ht "Оу… Тогда привет, меня зовут Хоси Такэути, будем знакомы."
    me "Д-да… Наверно… Хах?"
    ht "Ладно, новичок, еще увидимся."
    me "Пока… Хоси."
    "Какая же она... {w}добрая?"
    "Я вернулся на свой этаж и стал дожидаться следующей посылки."
    "Почему мы передаём посылки с этажа на этаж? Почему нельзя выходить в другие дни, кроме воскресенья? Сколько здесь этажей? Эти вопросы не давали мне покоя, но…"
    "Я, черт{w} возьми, в Cloud Inc."

    window hide
    play sound nyaa
    $renpy.pause(0.8)
    window show

    "А? Что это?"
    "Я подошел к окну, на подоконнике лежала записка:"
    "{i}«Пожалуйста, помоги мне! Достань из следующей посылки маячок и сбрось его мне в окно»{/i}"
    "Прежде, чем я успел о чем-либо подумать, ко мне постучались."
    rab "Снова на 274.2."
    me "Х-хорошо…"
    "А вот и следующая посылка. И что мне теперь делать?"

    window hide
    $ renpy.pause(0.5)
    menu:
        "Передать на 274.2":
            jump give
        "Вскрыть":
            jump open

label give:

    "Конечно, передать дальше! Не буду же я нарушать правила, тем более в первый же день. "
    "Я снова отправился на этаж выше. Лифт, на удивление, не сразу открылся..."

    scene black
    with dissolve
    scene vorota
    with dissolve
    
    n "А вон то облако было в форме пирога. "
    n "Ты видел его?"
    n "Жаль, что оно тоже расплылось, но ведь… облаков же много, да?"
    n "Их ведь много?.."
    nvl clear

    scene black
    with dissolve
    scene vorota
    with dissolve

    "Двери лифта распахнулись."

label open:

    $ prolog += 1

    "Думаю, стоит рискнуть и довериться записке."
    "Я аккуратно отклеил скотч и открыл картонную коробку. В ней и вправду лежал маячок. Он светился красным огоньком и мигал вторым - зеленым. "
    "Не став долго его разглядывать, я сбросил маячок с окна. Неужели кто-то реально его словит?"
    "Я заклеил обратно коробку и отправился на 274.2."


label posilka:

    ht "И снова привет!"
    me "Здравствуй. Вот посылка."
    ht "Как тебе первый рабочий день?"
    me "Ну… непривычно."
    ht "Понимаю тебя, я тоже первый день нервничала."
    me "Давно ты здесь работаешь?"
    ht "…"
    me "Ладно, забылась наверное?"
    ht "Д-да, именно."
    me "Ну, с кем не бывает."
    ht "Наверно, ты прав."
    ht "Слушай, наши смены завершаются в 7, не хочешь вместе поужинать?"
    me "…"

    window hide
    $ renpy.pause(0.5)
    menu:
        "Передать на 274.2":
            jump busy
        "Вскрыть":
            jump date

label busy:

    me "У меня другие планы."
    ht "Ничего, я понимаю, первый день. Тогда удачи тебе!"
    me "Спасибо."
    "Я вернулся в кабинет. При следующих встречах мы с Хоси особо не разговаривали. Я отдавал посылку…{w} и возвращался к себе."
    "7 вечера. Эх… Мы бы сейчас могли ужинать с Хоси. "
    "И что теперь делать? "
    "Интересно, сколько здесь этажей? Я старался не думать об этом, но любопытство взяло своё. "
    "Я зашел в лифт."
    me "500-тый этаж."
    "Лифт открылся. "
    "«500.1», «500.2», «500.3»."
    "Как это здание может быть настолько огромным?"
    me "999-ый этаж."
    "Лифт открылся."
    me "9999-ый."
    "Снова."
    me "1462384-ый этаж."
    "Открылся… И каждый раз 3 двери."
    "Я вернулся на свой этаж."
    "Уже собираясь войти в свой кабинет, я, интереса ради, постучался в соседний 273.1."
    "Тишина. То же было и с 273.3."
    "Не выдержав, я открыл дверь. 273.1, и здесь… тот самый работник?!"
    rab "Не отвлекай других сотрудников."
    me "Ты ведь с другого этажа!"
    rab "Я сказал…"
    me "Я звоню в администрацию..!"
    "Не успев закончить свою фразу, я с ужасом стал наблюдать за тем, как работник вылезает в окно."
    rab "Не ту работу ты выбрал, удачи."
    play sound unravel
    "Он спрыгнул… {w}{cps=8.5}и полетел вниз…{/cps}"

    window hide
    $renpy.pause(3)

    jump ed

label date:

    $ prolog += 1

    me "Д-да... с радостью!"
    ht "Отлично! Тогда, после смены, я у тебе приду."
    me "Хорошо."
    "Обалдеть. В первый же день я буду ужинать с милой девушкой. "
    "Надо хорошенько подготовиться."
    "7 вечера. "
    "Итак. Я успел принарядиться, накрыл небольшой стол."
    "Она любит шампанское? Ладно, достану бутылку."

    window hide
    play sound knock
    $renpy.pause(0.8)
    window show

    "Кажется, это она."
    ht "Привет~!"
    "Она… завораживает."
    me "..Проходи."
    ht "Ты так уютно устроился, молодец!"
    me "Спасибо."
    "Мы сели за стол и принялись наедаться рисовыми шариками."
    "Мы болтали об учебе, о доме, о родных, обсуждали забавные истории из жизни."
    ht "Ты знаешь, по сравнению с прошлым работником 273.2, ты лучший!"
    me "Правда?"
    "Хоси закрыла глаза, её лицо стало ко мне приближаться, а губы приоткрылись. "
    "Мы ведь с ней только познакомились, неужели в первый же день?"
    "Я закрыл глаза. Этот поцелуй был несравним с моими школьными романами."
    "Но, не успев прочувствовать, Хоси оттолкнула меня и убежала из кабинета на свой этаж."
    "Я сделал что-то не так? Но что?"
    "В горечи я налил бокал нетронутого шампанского и пил… "
    "Пока в итоге не заснул."
    "Среди ночи я резко встал."
    "Я, наверно, виноват перед Хоси. Надо хотя бы извиниться…"
    "Я поднялся к ней, открыл дверь, но она…"
    "{cps=8.5}Она… пов… повесилась…{/cps}"
    play sound negr

    window hide
    $renpy.pause(10)

    jump ed

label ed:

    scene black
    with dissolve

    if prolog == 3:

        n "Я вспомнил. Я вспомнил, какой формы был третье облако."
        n "Оно было в форме звёздочки."
        n "Теперь я знаю, почему оно расплылось."
        n "Спасибо тебе… {w}И удачи в Cloud Inc."

        nvl clear

        return

    elif prolog == 0:
        n "Проверка от лица Cloud Inc завершена. Вы нам не подходите."
        n "Окно ждет вас в вашем кабинете. Всего хорошего."
        n "Спасибо, что поработали в Cloud Inc."

        nvl clear

        return

    else:

        n "Как тебе твой первый день, нравится?"
        n "Но не вздумай расслабляться. Мы только начинаем."
        n "Удачи в Cloud Inc."

        nvl clear

        return
