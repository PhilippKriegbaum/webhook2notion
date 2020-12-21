
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, wr_title, wr_date, wr_kind, wr_customer, wr_hours, wr_details, wr_remote):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.Name = wr_title
    row.Datum = wr_date
    row.Art = wr_kind
    row.Kunde = wr_customer
    row.Stunden = wr_hours
    row.Beschreibung = wr_details
    row.Remote = wr_remote


@app.route('/create_workingrecord', methods=['GET'])
def create_workingrecord():

    wr_title = request.args.get('title')
    wr_date = request.args.get('date')
    wr_kind = request.args.get('kind')
    wr_customer = request.args.get('customer')
    wr_hours = request.args.get('hours')
    wr_details = request.args.get('details')
    wr_remote = request.args.get('remote')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, wr_title, wr_date, wr_kind, wr_customer, wr_hours, wr_details, wr_remote)
    return f'added {wr_title} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
