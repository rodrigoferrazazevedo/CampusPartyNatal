# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("localhost", 1883)
mqttc.publish("hello/world", "Campus Party Natal")
mqttc.loop(2)
