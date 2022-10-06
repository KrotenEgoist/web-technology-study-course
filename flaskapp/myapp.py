from flask import Flask, jsonify, render_template
from flask_cors import CORS
import asyncio
from vkbottle.user import User
from random import randrange, choice
user = User("token")


loop = asyncio.get_event_loop()
app = Flask(__name__)
CORS(app)
async def get_photo(owner_id, album_id):
    try:
        owner_id=int(owner_id)
        album_id=[int(album_id)]
    except Exception as e:
        url = 'None'
        response_data = {
            'img_url': url
        }
        return jsonify(response_data)
    if (await user.api.photos.get_albums(owner_id=owner_id, album_ids=album_id)).count == 0:
        url = 'None'
    else:
        try:
            count = randrange((await user.api.photos.get(owner_id=owner_id, album_id=album_id, count=1)).count)
            t = choice((await user.api.photos.get(owner_id=owner_id, album_id=album_id, count=1, offset=count)).items)
            url = t.sizes[-1].url
        except Exception as e:
            print(e)
            url = 'None'
    response_data = {
        'img_url' : url
    }
    print(url)
    return jsonify(response_data)

@app.route('/get/owner_id=<owner_id>&album_id=<album_id>', methods=['GET'])
def get_rand(owner_id, album_id):
    return loop.run_until_complete(get_photo(owner_id, album_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
