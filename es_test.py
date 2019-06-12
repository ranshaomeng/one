from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'10.10.13.12','port':9200}])
es = Elasticsearch(['10.10.13.12'], timeout=3600)
es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')