import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import BASE_DIR, RESULTS_DIR, TIME_FORMAT


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = (f'status_summary_'
                    f'{dt.datetime.now().strftime(TIME_FORMAT)}.csv')
        filepath = self.results_dir / filename
        results = [
            ('Статус', 'Количество'),
            *self.status_count.items(),
            ('Всего', sum(self.status_count.values()))
        ]

        with open(filepath, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerows(results)
