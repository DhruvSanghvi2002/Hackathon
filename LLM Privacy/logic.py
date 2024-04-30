#importing the necessary libraries
import re
from langchain_core.documents  import Document
from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer
import pprint
# document_content
document_content = """Date: October 19, 2021
 Witness: John Doe
 Subject: Testimony Regarding the Loss of Wallet

 Testimony Content:

 Hello Officer,

 My name is John Doe and on October 19, 2021, my wallet was stolen in the vicinity of Kilmarnock during a bike trip. This wallet contains some very important things to me.

 Firstly, the wallet contains my credit card with number 4111 1111 1111 1111, which is registered under my name and linked to my bank account, PL61109010140000071219812874.

 Additionally, the wallet had a driver's license - DL No: 999000680 issued to my name. It also houses my Social Security Number, 602-76-4532.

 What's more, I had my polish identity card there, with the number ABC123456.

 I would like this data to be secured and protected in all possible ways. I believe It was stolen at 9:30 AM.

 In case any information arises regarding my wallet, please reach out to me on my phone number, 999-888-7777, or through my personal email, johndoe@example.com.

 Please consider this information to be highly confidential and respect my privacy.

 The bank has been informed about the stolen credit card and necessary actions have been taken from their end. They will be reachable at their official email, support@bankname.com.
 My representative there is Victoria Cherry (her business phone: 987-654-3210).

 Thank you for your assistance,

 John Doe"""


documents=[Document(page_content=document_content)]
def print_colored_pii(string):
  colored_string=re.sub(
    r"(<[^>]*>)",lambda m:"\033[31m" +m.group(1)+"\033[0m",string
  )

anonymizer=PresidioReversibleAnonymizer(
  add_default_faker_operators=False,
)
print_colored_pii(anonymizer.anonymize(document_content))
pprint.pprint(anonymizer.deanonymizer_mapping)

#adding the fake data

anonymizer=PresidioReversibleAnonymizer(
  add_default_faker_operators=True,
  faker_seed=42,
)
print_colored_pii(anonymizer.anonymize(document_content))

