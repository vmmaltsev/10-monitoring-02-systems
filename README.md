# Домашнее задание к занятию 13 «Системы мониторинга» - `Мальцев Виктор`

---

Обязательные задания

---

1. Вас пригласили настроить мониторинг на проект. На онбординге вам рассказали, что проект представляет из себя платформу для вычислений с выдачей текстовых отчетов, которые сохраняются на диск. Взаимодействие с платформой осуществляется по протоколу http. Также вам отметили, что вычисления загружают ЦПУ. Какой минимальный набор метрик вы выведите в мониторинг и почему?

Ответ:

Для настройки мониторинга важно отслеживать несколько ключевых метрик, которые помогут обеспечить надежную и эффективную работу системы. Вот минимальный набор метрик, которые я бы рекомендовал:

1. CPU Usage (Загрузка ЦПУ): Поскольку вычисления загружают ЦПУ, важно отслеживать использование ЦПУ. Это поможет определить, достаточно ли мощности процессора для текущей нагрузки и необходимо ли масштабирование или оптимизация процессов.

2. Memory Usage (Использование памяти): Помимо ЦПУ, следует мониторить и использование оперативной памяти, чтобы убедиться, что система не достигает предела своих возможностей и не теряет производительности.

3. Disk Usage/IO (Использование диска и дисковые операции): Так как отчеты сохраняются на диск, важно отслеживать не только свободное место на диске, но и интенсивность дисковых операций. Это поможет предотвратить проблемы с производительностью или потерю данных из-за нехватки места.

4. HTTP Requests (HTTP-запросы): Мониторинг HTTP-запросов поможет понять, как часто и как интенсивно используется платформа. Это включает в себя количество запросов, время ответа, ошибки и статусы ответов.

5. Error Rates (Частота ошибок): Важно отслеживать ошибки как в коде, так и в инфраструктуре, чтобы быстро реагировать на проблемы и обеспечить стабильность системы.

6. Network Traffic (Сетевой трафик): Мониторинг входящего и исходящего трафика поможет определить аномалии и потенциальные проблемы безопасности.

Этот набор метрик позволит получить базовое понимание состояния системы, выявлять узкие места и предотвращать серьезные проблемы в работе платформы. В дополнение к этому, в зависимости от специфики проекта, могут потребоваться и другие метрики.

---

2. Менеджер продукта посмотрев на ваши метрики сказал, что ему непонятно что такое RAM/inodes/CPUla. Также он сказал, что хочет понимать, насколько мы выполняем свои обязанности перед клиентами и какое качество обслуживания. Что вы можете ему предложить?

Ответ:

Понимание запроса менеджера продукта важно для эффективного мониторинга. Ему нужны более понятные и релевантные метрики, которые могут отражать качество обслуживания и выполнение обязательств перед клиентами. Вот несколько предложений:

1. Время отклика системы (Response Time): Это время, которое требуется системе, чтобы обработать запрос и вернуть результат. Это критический показатель для пользовательского опыта.

2. Процент успешных запросов (Success Rate): Это показывает, какая доля запросов к системе обрабатывается успешно без ошибок. Это может включать успешную генерацию и сохранение отчетов.

3. Число и типы ошибок (Error Types and Rates): Важно понимать, какие ошибки возникают и с какой частотой, чтобы определить, как они влияют на клиентский опыт.

4. Среднее время обработки запроса (Average Processing Time): Это время, необходимое для выполнения типичного запроса или операции. Это помогает оценить эффективность и производительность системы.

5. Доступность сервиса (Service Availability): Это процент времени, когда сервис доступен для использования. Высокий уровень доступности критичен для доверия клиентов.

6. Пропускная способность системы (Throughput): Количество операций или запросов, которые система может обработать за определенный период времени. Это отражает способность системы справляться с нагрузкой.

7. Пользовательское удовлетворение (User Satisfaction): Опросы или обратная связь от клиентов могут быть использованы для оценки общего удовлетворения клиентов.

Эти метрики более ориентированы на бизнес-перспективу и могут помочь менеджеру продукта понять, насколько хорошо продукт соответствует потребностям и ожиданиям клиентов. Они также помогут выявить области для улучшения и оптимизации.

---

3. Вашей DevOps команде в этом году не выделили финансирование на построение системы сбора логов. Разработчики в свою очередь хотят видеть все ошибки, которые выдают их приложения. Какое решение вы можете предпринять в этой ситуации, чтобы разработчики получали ошибки приложения?

Ответ:

В ситуации с ограниченным финансированием для построения системы сбора логов, можно рассмотреть несколько альтернативных подходов, которые помогут разработчикам получать информацию об ошибках приложения:

1. Использование Open-Source Решений: Существует множество бесплатных и открытых инструментов для сбора и анализа логов, таких как ELK Stack (Elasticsearch, Logstash, Kibana) или Graylog. Эти системы требуют некоторых усилий для настройки и поддержки, но они предлагают гибкие и мощные возможности для работы с логами.

2. Локальное Хранение и Анализ Логов: Если нет возможности использовать централизованные системы, можно настроить локальное хранение логов на серверах приложений с регулярным ротированием и архивацией. Разработчики могут получать доступ к этим логам по запросу или через автоматизированные скрипты.

3. Интеграция с Системами Управления Инцидентами: Если у компании уже есть система управления инцидентами (например, JIRA, Redmine), можно настроить автоматическое создание задач на основе ошибок, фиксируемых в логах приложений.

4. Использование Облачных Сервисов: Многие облачные провайдеры предлагают бесплатные или недорогие решения для сбора и анализа логов. Эти сервисы могут быть альтернативой при отсутствии собственной инфраструктуры.

5. Разработка Простого Внутреннего Решения: Возможно создание простой внутренней системы для сбора и распределения логов с использованием скриптов и базовых инструментов, таких как rsync, cron jobs и простые базы данных или файловые системы для хранения логов.

6. Регулярные Отчеты и Алерты: Можно настроить скрипты или задачи, которые регулярно анализируют логи на наличие ошибок и отправляют отчеты или уведомления разработчикам.

Выбор подхода зависит от конкретных потребностей команды, наличия ресурсов для поддержки и управления системой сбора логов, а также от требований к безопасности и конфиденциальности данных.

---

4. Вы, как опытный SRE, сделали мониторинг, куда вывели отображения выполнения SLA=99% по http кодам ответов. Вычисляете этот параметр по следующей формуле: summ_2xx_requests/summ_all_requests. Данный параметр не поднимается выше 70%, но при этом в вашей системе нет кодов ответа 5xx и 4xx. Где у вас ошибка?

Ответ:

Основываясь на описанной формуле для расчета выполнения SLA (Service Level Agreement) по HTTP-кодам ответов, есть потенциальная проблема, которая может объяснить, почему показатель не поднимается выше 70%, даже если в системе отсутствуют коды ответов 5xx и 4xx.

Формула summ_2xx_requests / summ_all_requests учитывает только запросы, которые привели к успешным ответам (коды 2xx). В HTTP присутствуют и другие категории ответов, которые могут считаться "успешными" в контексте работы приложения, но не включены в вашу формулу. Например:

   Коды 3xx (Перенаправления): Эти коды говорят о том, что клиенту нужно выполнить дополнительные действия для завершения запроса. Во многих случаях, это нормальное поведение (например, 301 Moved Permanently или 302 Found).

   Коды 1xx (Информационные): Хотя они редко используются, они также могут встречаться в нормальной работе веб-приложений.

Если расчеты SLA не учитывают эти дополнительные категории успешных запросов, это может привести к заниженному показателю выполнения SLA. Для более точного отображения SLA вам, возможно, стоит пересмотреть определение "успешного" запроса в контексте вашего приложения и включить в расчеты соответствующие категории HTTP-кодов.

Например, формула может быть переопределена как:

```
(summ_2xx_requests + summ_3xx_requests) / summ_all_requests
```

или даже

```
(summ_2xx_requests + summ_3xx_requests + summ_1xx_requests) / summ_all_requests
```

в зависимости от того, какие категории ответов считаются "успешными" в контексте работы веб-приложения.

---

5. Опишите основные плюсы и минусы pull и push систем мониторинга.

Ответ:

Push-метод
Плюсы:

    Активная отправка данных: Узлы или агенты активно отправляют данные на сервер мониторинга, что может обеспечить более своевременное обновление информации.
    Масштабируемость: Легко добавлять новые узлы в систему мониторинга, так как каждый узел сам отправляет данные.
    Гибкость в отчетности: Узлы могут настраивать частоту и объем отправляемых данных в зависимости от своих нужд.
    Обход сетевых ограничений: Подходит для ситуаций, где узлы находятся за NAT или фаерволами, так как инициация соединения происходит изнутри сети.

Минусы:

    Управление конфигурацией: Требуется отдельная настройка каждого узла или агента, что может быть сложно при большом количестве узлов.
    Проблемы с безопасностью: Открытие сервера мониторинга для входящих соединений может увеличить риски безопасности.
    Потенциальная перегрузка данных: Возможность перегрузки сервера мониторинга из-за большого количества входящих данных.
    Обнаружение отказов узлов: Трудно определить, вышел ли узел из строя или просто перестал отправлять данные.

Pull-метод
Плюсы:

    Централизованное управление: Все настройки и политики сбора данных управляются централизованно.
    Безопасность: Безопаснее, так как сервер мониторинга инициирует соединение, и не требуется открытых портов на узлах.
    Стабильность и предсказуемость: Сервер контролирует частоту и объем сбора данных, что уменьшает риск перегрузки.
    Легче обнаружить проблемы с узлами: Если узел не отвечает на запросы, это сразу же становится ясно.

Минусы:

    Ограничения сетевого доступа: Может быть сложно получить данные от узлов, находящихся за фаерволами или NAT.
    Задержка данных: Может быть некоторая задержка между сбором данных и их отображением, в зависимости от настройки частоты запросов.
    Сложности масштабирования: Добавление новых узлов требует изменений в конфигурации центрального сервера.
    Нагрузка на сеть: Высокая частота опроса узлов может создавать дополнительную нагрузку на сеть.

---

6. Какие из ниже перечисленных систем относятся к push модели, а какие к pull? А может есть гибридные?

    Prometheus
    TICK
    Zabbix
    VictoriaMetrics
    Nagios

Ответ: 

Чтобы классифицировать эти системы мониторинга (Prometheus, TICK, Zabbix, VictoriaMetrics, и Nagios) как относящиеся к моделям push, pull, или гибридным, рассмотрим их основные характеристики:

    Prometheus: Это система, использующая в основном модель pull, что означает, что Prometheus активно запрашивает (или "вытягивает") данные с мониторируемых устройств или приложений. Однако она также поддерживает push-модель через Pushgateway для сценариев, когда устройства не могут быть легко опрошены.

    TICK (Telegraf, InfluxDB, Chronograf, Kapacitor): В этом стеке Telegraf обычно используется для сбора метрик, который может работать как в pull, так и в push режимах. Таким образом, TICK может быть классифицирован как гибридная система.

    Zabbix: Zabbix поддерживает как pull, так и push модели. Агенты Zabbix могут быть настроены на отправку данных (push) или на их опрос (pull) сервером Zabbix.

    VictoriaMetrics: Это высокопроизводительная база данных для хранения временных рядов, совместимая с Prometheus. Она поддерживает push-модель, поскольку данные могут быть отправлены в нее, но также может извлекать данные из Prometheus, работающего в pull-модели, делая ее гибридной.

    Nagios: Традиционно Nagios использует pull-модель, где сервер Nagios опрашивает мониторируемые устройства. Однако существуют плагины и настройки, позволяющие реализовать push-модель.

Итак, подытоживая:

    Prometheus и Nagios в основном используют pull-модель, но могут поддерживать push в определенных конфигурациях.

    TICK и VictoriaMetrics являются гибридными системами, поддерживающими как push, так и pull.
    
    Zabbix поддерживает обе модели, делая его также гибридной системой.

---

7. Склонируйте себе репозиторий и запустите TICK-стэк, используя технологии docker и docker-compose.
В виде решения на это упражнение приведите скриншот веб-интерфейса ПО chronograf (http://localhost:8888).

P.S.: если при запуске некоторые контейнеры будут падать с ошибкой - проставьте им режим Z, например ./data:/var/lib:Z

Ответ:

![alt text](https://github.com/vmmaltsev/screenshot/blob/main/Screenshot_86.png)

---

8. Перейдите в веб-интерфейс Chronograf (http://localhost:8888) и откройте вкладку Data explorer.

Нажмите на кнопку Add a query
Изучите вывод интерфейса и выберите БД telegraf.autogen
В measurments выберите cpu->host->telegraf-getting-started, а в fields выберите usage_system. Внизу появится график утилизации cpu.
Вверху вы можете увидеть запрос, аналогичный SQL-синтаксису. Поэкспериментируйте с запросом, попробуйте изменить группировку и интервал наблюдений.
Для выполнения задания приведите скриншот с отображением метрик утилизации cpu из веб-интерфейса.

Ответ:

![alt text](https://github.com/vmmaltsev/screenshot/blob/main/Screenshot_87.png)

---

9. Изучите список telegraf inputs. Добавьте в конфигурацию telegraf следующий плагин - docker:
[[inputs.docker]]
  endpoint = "unix:///var/run/docker.sock"
Дополнительно вам может потребоваться донастройка контейнера telegraf в docker-compose.yml дополнительного volume и режима privileged:

  telegraf:
    image: telegraf:1.4.0
    privileged: true
    volumes:
      - ./etc/telegraf.conf:/etc/telegraf/telegraf.conf:Z
      - /var/run/docker.sock:/var/run/docker.sock:Z
    links:
      - influxdb
    ports:
      - "8092:8092/udp"
      - "8094:8094"
      - "8125:8125/udp"
После настройке перезапустите telegraf, обновите веб интерфейс и приведите скриншотом список measurments в веб-интерфейсе базы telegraf.autogen . Там должны появиться метрики, связанные с docker.

Факультативно можете изучить какие метрики собирает telegraf после выполнения данного задания.

Ответ:

![alt text](https://github.com/vmmaltsev/screenshot/blob/main/Screenshot_88.png)


---

Дополнительное задание (со звездочкой*) - необязательно к выполнению
Вы устроились на работу в стартап. На данный момент у вас нет возможности развернуть полноценную систему мониторинга, и вы решили самостоятельно написать простой python3-скрипт для сбора основных метрик сервера. Вы, как опытный системный-администратор, знаете, что системная информация сервера лежит в директории /proc. Также, вы знаете, что в системе Linux есть планировщик задач cron, который может запускать задачи по расписанию.
Суммировав все, вы спроектировали приложение, которое:

является python3 скриптом

собирает метрики из папки /proc

складывает метрики в файл 'YY-MM-DD-awesome-monitoring.log' в директорию /var/log (YY - год, MM - месяц, DD - день)

каждый сбор метрик складывается в виде json-строки, в виде:

timestamp (временная метка, int, unixtimestamp)

metric_1 (метрика 1)

metric_2 (метрика 2)

...

metric_N (метрика N)

сбор метрик происходит каждую 1 минуту по cron-расписанию

Для успешного выполнения задания нужно привести:

а) работающий код python3-скрипта,

б) конфигурацию cron-расписания,

в) пример верно сформированного 'YY-MM-DD-awesome-monitoring.log', имеющий не менее 5 записей,

P.S.: количество собираемых метрик должно быть не менее 4-х. P.P.S.: по желанию можно себя не ограничивать только сбором метрик из /proc.

Ответ:

Для успешного выполнения задания нужно привести:

а) работающий код python3-скрипта

```

import json
import time
from datetime import datetime
import os

def get_network_connections():
    with open('/proc/net/tcp', 'r') as f:
        return len(f.readlines()) - 1  # Вычитаем одну строку заголовка

def get_cpu_count():
    return os.cpu_count()

def get_swap_size():
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if line.startswith('SwapTotal'):
                return int(line.split()[1])

def collect_metrics():
    timestamp = int(time.time())
    uptime = float(open('/proc/uptime').readline().split()[0])
    load_avg = open('/proc/loadavg').readline().split()[:3]
    memory_total = float(open('/proc/meminfo').readline().split()[1])
    
    network_connections = get_network_connections()
    cpu_count = get_cpu_count()
    swap_size = get_swap_size()

    metrics = {
        "timestamp": timestamp,
        "uptime": uptime,
        "load_avg": load_avg,
        "memory_total_kb": memory_total,
        "network_connections": network_connections,
        "cpu_count": cpu_count,
        "swap_size_kb": swap_size
    }

    log_filename = datetime.now().strftime("/var/log/%Y-%m-%d-awesome-monitoring.log")
    with open(log_filename, "a") as log_file:
        log_file.write(json.dumps(metrics) + "\n")

if __name__ == "__main__":
    collect_metrics()

```

б) конфигурацию cron-расписания

```

* * * * * /usr/bin/python3 /root/mon/monitoring.py

```

в) пример верно сформированного 'YY-MM-DD-awesome-monitoring.log', имеющий не менее 5 записей

```

{"timestamp": 1699963561, "uptime": 9824.99, "load_avg": ["0.04", "0.07", "0.03"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963622, "uptime": 9885.05, "load_avg": ["1.43", "0.43", "0.15"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963681, "uptime": 9944.11, "load_avg": ["0.61", "0.38", "0.15"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963741, "uptime": 10004.15, "load_avg": ["0.38", "0.34", "0.15"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963801, "uptime": 10064.2, "load_avg": ["0.14", "0.28", "0.14"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963861, "uptime": 10124.25, "load_avg": ["0.05", "0.22", "0.13"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963921, "uptime": 10184.94, "load_avg": ["0.17", "0.24", "0.14"], "memory_total_kb": 2014480.0, "network_connections": 19, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699963981, "uptime": 10245.0, "load_avg": ["0.06", "0.19", "0.13"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}
{"timestamp": 1699964042, "uptime": 10305.05, "load_avg": ["0.02", "0.16", "0.11"], "memory_total_kb": 2014480.0, "network_connections": 18, "cpu_count": 2, "swap_size_kb": 0}

```


---



