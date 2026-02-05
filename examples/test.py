from doubaoime_asr.sami import get_sami_token
from doubaoime_asr.ner import get_ner_results
from doubaoime_asr.wave_client import WaveClient
from doubaoime_asr.constants import AID


device_id = "1875114961702217"
app_id = AID

token = get_sami_token()
print(token)

wave_client = WaveClient(device_id, app_id)
ner_results = get_ner_results(wave_client, token, "张三李四以及张三本人", device_id)
print(ner_results)

