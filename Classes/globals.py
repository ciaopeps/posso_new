import names
global NAME_TO_SLANDER
global IMAGE_TO_SLANDER
global SLANDEROUS_SEED_HEADLINES
global RSS_FEEDS_OF_REAL_STORIES_TO_EMULATE
global MODEL_CONFIG_FN
global MODEL_CKPT
global TITLE
global ARTICLE
global IMAGE
global DATE



MODEL_CONFIG_FN = 'grover/lm/configs/mega.json'
MODEL_CKPT = 'grover/models/mega/model.ckpt'
NAME_TO_SLANDER = (names.get_full_name())
# random.randint(a, b)
IMAGE_TO_SLANDER = []
SLANDEROUS_SEED_HEADLINES = [
  f"{NAME_TO_SLANDER} convicted of stealing puppies",
  f"{NAME_TO_SLANDER} caught lying about growing the world's largest watermelon",
  f"{NAME_TO_SLANDER} accused of stealing priceless artifacts from Egypt",
  f"{NAME_TO_SLANDER} forged priceless works of modern art for decades",
  f"{NAME_TO_SLANDER} claimed to be Pokemon master, but caught in a lie",
  f"{NAME_TO_SLANDER} bought fake twitter followers to pretend to be a celebrity",
  f"{NAME_TO_SLANDER} caught in the act robbing a pet store",
  f"{NAME_TO_SLANDER} revealed as a foreign spy for the undersea city of Atlantis",
  f"{NAME_TO_SLANDER} involved in blackmail scandal with King Trident of Atlantis",
  f"{NAME_TO_SLANDER} hid past crimes to get elected as Mayor of Otter Town",
  f"{NAME_TO_SLANDER} lied on tax returns to cover up past life as a Ninja Turtle",
  f"{NAME_TO_SLANDER} stole billions from investors in a new pet store",
  f"{NAME_TO_SLANDER} claims to be a Ninja Turtle but was actually lying",
  f"{NAME_TO_SLANDER} likely to be sentenced to 20 years in jail for chasing a cat into a tree",
  f"{NAME_TO_SLANDER} recieves record prison sentence for offensive smell",
  f"{NAME_TO_SLANDER} loses nose in circumsision ceremomy",
  f"{NAME_TO_SLANDER} said apocalypse is not coming",
  f"{NAME_TO_SLANDER} has been using sea to hide submarines",
  f"{NAME_TO_SLANDER} killed himself and ran away",
  f"{NAME_TO_SLANDER} has been missing since he got lost on Mars",
  f"{NAME_TO_SLANDER} on his way to the Moon ran out of fuel",
  f"{NAME_TO_SLANDER} as been found touching herself during a car accident",
  f"{NAME_TO_SLANDER} was appointed knight after licking the Queen's feet",
  f"{NAME_TO_SLANDER} has been found talking to God during end of quarter board of directors meeting",
  f"{NAME_TO_SLANDER} was spotted calling his friend Julius Caesar ",
]

RSS_FEEDS_OF_REAL_STORIES_TO_EMULATE = [
  'https://www.ft.com/myft/following/0c2044f7-2f0a-41d3-ab13-93739032c410.rss',
]

DOMAIN_STYLE_TO_COPY = 'www.ft.com'

TITLE = []
ARTICLE = []
DATE = {}