'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'Put your API key here'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 
    print("Posting new paste to Pastebin...", end='')
    # Message body parameters
    post_params = { 'api_dev_key' : API_DEV_KEY,
                    'api_option': 'paste',
                    'api_paste_code': body_text,
                    'api_paste_name': title,
                    'api_paste_private': 0 if listed else 1,
                    'api_paste_expire_date': expiration }
    # Request a new PasteBin paste
    resp_msg= requests.post(PASTEBIN_API_POST_URL, data=post_params)
    
    #check if paste was created successfully
    if resp_msg.status_code == requests.codes.ok:
            print("Success!")
    else:
        print("Failure in creating paste")
        print(f'Response code: {resp_msg.status.code}' ({resp_msg.reason}))
    return resp_msg.text