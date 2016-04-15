import vkontakte
import vk_auth
import getpass

snob_parser_id = '5161360'
snob_group_id = '-101947002'
my_login = ''
my_password = getpass.getpass()

access_token = vk_auth.auth(my_login, my_password, snob_parser_id, "audio,status")[0]

vk = vkontakte.API(token=access_token)
all_tunes_in_public = vk.audio.get(owner_id=snob_group_id)

# for tune in all_tunes_in_public:
#     for tune_field in tune



