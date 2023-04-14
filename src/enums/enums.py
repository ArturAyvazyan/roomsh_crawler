import enum


class LegalForms(enum.Enum):
    SELF_EMPLOYED: "Самозанятый"
    IP: "ИП"
    OOO: "ООО"


class Cities(enum.Enum):
    SAINT_PETERSBURG: "Saint Petersburg"
    MOSCOW: "Moscow"
    NIZHNY_NOVGOROD: "Nizhny Novgorod"
    NOVOSIBIRSK: "Novosibirsk"
    YEKATERINBURG: "Yekaterinburg"
    KAZAN: "Kazan"
    CHELYABINSK: "Chelyabinsk"
    KRASNOYARSK: "Krasnoyarsk"
    SAMARA: "Samara"
    UFA: "Ufa"
    ROSTOV_ON_DON: "Rostov on Don"
    OMSK: "Omsk"
    KRASNODAR: "Krasnodar"
    VORONEZH: "Voronezh"
    VOLGOGRAD: "Volgograd"
    PERM: "Perm"


class ShroomType(enum.Enum):
    TUBER: "Трюфели"
    BOLETUS: "Боровик"
    GANODERMA_LUCIDUM: "Рейши"
    PHALLUS_IMPUDICUS: "Веселка"
    CANTHARELLUS_CIBARIUS: "Лисичка"
    KOMBUCHA: "Комбуча"
    HERICIUM_ERINACEUS: "Ежовик гребенчатый"
    CORDYCEPS: "Кордицепс"
    INONOTUS_OBLIQUUS: "Чага Березовая"
    ARMILLARIA_MELLEA: "Опёнок"
    AMANITA_MUSCARINA: "Мухомор Красный"
    AMANITA_PANTHERINA: "Мухомор Пантерный"
