kafka=/home/joe/Downloads/kafka_2.12-1.0.0
gnome-terminal -e "$kafka'/bin/zookeeper-server-start.sh' $kafka'/config/zookeeper.properties'"
gnome-terminal -e "$kafka'/bin/kafka-server-start.sh' $kafka'/config/server.properties'"
gnome-terminal -e "$kafka'/bin/kafka-console-consumer.sh' --bootstrap-server localhost:9092 --topic test --from-beginning"
env/bin/python main.py