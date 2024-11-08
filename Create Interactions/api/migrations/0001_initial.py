# Generated by Django 5.1.2 on 2024-10-30 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_up_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_by', models.IntegerField()),
                ('img', models.BinaryField()),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_duration', models.CharField(max_length=20)),
                ('staffs', models.CharField(max_length=500)),
                ('c_details', models.CharField(max_length=5000)),
                ('c_books', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='log_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.IntegerField()),
                ('user2', models.IntegerField()),
                ('receive', models.CharField(max_length=500)),
                ('send', models.CharField(max_length=500)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.BinaryField(default=b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\t\x06\x07\x08\x07\x06\t\x08\x07\x08\n\n\t\x0b\r\x16\x0f\r\x0c\x0c\r\x1b\x14\x15\x10\x16 \x1d"" \x1d\x1f\x1f$(4,$&1\'\x1f\x1f-=-157:::#+?D?8C49:7\x01\n\n\n\r\x0c\r\x1a\x0f\x0f\x1a7%\x1f%77777777777777777777777777777777777777777777777777\xff\xc0\x00\x11\x08\x00\x90\x00\xc8\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1c\x00\x01\x00\x01\x05\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x01\x04\x05\x06\x07\x03\x02\xff\xc4\x00;\x10\x00\x01\x03\x03\x01\x03\x08\x06\t\x05\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x11\x06\x07!A\x12\x171QUq\x92\xd1\x13"ar\x81\x91\x1523R\x82\xa1\xb1\xc1\xe1\x086t\xe2\xf1$\xff\xc4\x00\x14\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc4\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xee \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\xc8\x0c\x96w+\xb5\xbe\xd7\x17\xa5\xb8\xd6\xd3\xd3G\xc1\xd2\xc8\x8d\xcfvNy\xb5}\xa67L\xa2\xda\xad\x1c\x89.\xaen^\xf5\xde\x90\'_\xbcG\x8b\x95\xd2\xba\xebT\xfa\xab\x95L\xb53\xbdr\xe9%vW\xf8\xf8\x01*\xf9\xca\xd1\xbe\x93\xd1\xfd?K\xca\xfcX\xf9\xe0\xcf\xdbn\xd6\xfb\xa4^\x96\xdd[OS\x1f\x17E";\x1d\xf8!Vwt\x17v\xdb\xa5u\xaa\xa9\x95V\xda\x99i\xa7b\xe5\xb2D\xec/\xf3\xf1\x02kd\xa9\xcb\xf6Q\xb4\xc6\xeadKU\xdf\x91\x1d\xd5\xad\xcb\x1e\x9b\x92t\xeb\xf7\x8e\x9f\x90*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00b\xb55\xd5\x96;\x05u\xd2N\x8aX\\\xf4N\xb5\xe0\x9f<!\x954=\xb7:F\xec\xe6\xe3\xc8\xcae\xd1\xa3\xb1\xd5\xcb@#\x15\xc6\xba\xa2\xe3]Q[V\xf5|\xf3\xbd_#\x97\x8a\xa9j\x00\x00\x00\x17V\xea\xea\x8buu=m#\xd5\x93\xc0\xf4|nN\n\x84\xc4\xd37V_,\x14\x17H\xfa*\xa1k\xd5:\x97\x8a|\xf2\x841%>\xc4\x9c\xf7l\xe6\xdc\x92gs\xa4F\xe7\xab\x96\xbf\xc8\x1b\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x83\xd6v\x8f\xa7\xb4\xbd\xc6\xd6\x98\xe5\xcf\x02\xb5\x9e\xfaoo\xe6\x86p\xa6\x00\x84S\xc1%<\xaf\x8af\xabdc\x95\xaej\xa6\xf4T\xe9C\xc8\xef[`\xd9\x8c\xd7\n\x89/\xfaz.T\xeeL\xd5S3\xa5\xeb\xf7\x9b\xed\xebC\x84I\x14\x91=\xcc\x91\x8ec\xdb\xb9\xcdraS\xbc\x0f\x80W\x1b\xcf\xa8\xe2\x92W\xb5\x91\xb1\xcf{\xb75\xadL\xaa\xf7\x01\xf5\x04\x12TJ\xc8\xa1j\xbaG\xb9\x1a\xd6\xa2oU^\x84&\x16\x8b\xb4}\x01\xa5\xed\xb6\xb5\xc7.\x08Q\xaf\xf7\xd7{\xbf59\x96\xc7\xf6c5\xbe\xa2;\xfe\xa1\x8b\x93;S4\xb4\xcf\xe9b\xfd\xe7{z\x90\xed\x18\x02\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\xe5\x00\xc1\xae\xea\x1d\x0f\xa75\x13\x95\xf7Kd2L\xa9\xf6\xec\xf5$\xf1&\xf5\xf8\x9f:\x87^i\xbd:\xaee\xca\xe7\nN\x9d0F\xbc\xb7\xfc\x93\xa0\xd0\xee;{\xb4\xc6\xe5m\xbe\xd1W:p|\xafk\x11\x7fP2\xbc\xc8i\x1fI\xca\xff\x00\xdf\xc9\xfb\x9e\x9fw\xe8m:{C\xe9\xcd:\xe4}\xae\xd9\x0cs"}\xbb\xfdy<K\xbd>\x07,\xe7\xfe\\\xff\x00oG\xc9\xff\x00\'\xfdL\xad\xbbov\x99\x1e\x8d\xb8Z*\xe0N/\x89\xed~?@;\x06\n\x9a\xd6\x9e\xd7\x9aoQ+Ym\xb9\xc2\xb3\xafD\x12/!\xff\x00%\xe96NP\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb3\xba\\\xa9m6\xea\x8a\xfa\xe9\x12*x\x18\xaf{\x97\xa9\x00\xf2\xbe^\xe8,6\xf9k\xee\x93\xb6\x1ax\xd3z\xaa\xefU\xeaD\xe2\xa4z\xd7{\\\xbb_d\x92\x92\xce\xe7\xdb\xed\xdd\x1e\xa2\xe2YS\xad\xcb\xc3\xb9\r\x7fhZ\xd2\xb7X]\x9d4\xaettQ*\xa5=>w5\xbdk\xedSS\xc8\x15s\xdc\xe5W9UUW*\xab\xbf%3\xff\x00J\x00\x05rP\x01\xf4\xd7\xb9\xaa\x8ej\xaa*.QSv\x0e\x97\xa16\xb9v\xb1I\x1d%\xdd\xcf\xb8[\xba=u\xcc\xb1\'[W\x8fr\x9c\xc8\xae@\x9a6;\xdd\x05\xfa\xdf\x15}\xaev\xcdO"nT]\xe8\xbdJ\x9c\x14\xc8\x91\'g\xba\xd2\xb7G\xdd\x9b4Nt\x94R\xaa%E>w9\xbdi\xedBUZ\xeeT\xb7[}=}\x0c\x89-<\xecG\xb1\xc9\xd4\xa0^\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x0f\xfa\x81\xd5o\x9a\xb6-7I"\xfa(q-V\x17\xa5\xcb\xf5[\xf2\xdf\xdewZ\xca\x96Q\xd2MS.\xe8\xa1\x8d\xd29s\xc1\x13*C+\xe5\xca[\xbd\xde\xb6\xe3:\xe6J\x99\x9d#\xbe+\x9c\x01c\x92\x80\x00\x00\x00\x00\x00\x00\x01\\\x9d\x9b\xfa~\xd5n\x86\xb6]7W*\xacSfZ\\\xf0r}f\xa7zo\xef8\xc1\x7fc\xb9Kh\xbcQ\xdc`v$\xa6\x99\xb2&=\x8b\x9c\x015\x01\xe1GR\xca\xbaH*b\xdf\x1c\xd1\xb6F\xaa/\x05L\xa1\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\xab\xb5\n\xa7Q\xe8\x0b\xe4\x8c\\9iU\x89\xf8\xbd_\xdc\x88\xf8&\xb5\xd6\xd9Iw\xa1\x96\x86\xe3\x0bg\xa5\x97s\xe3vp\xbcx\x1a\xdf6\x1a/\xb0i\xfcN\xf3\x02&\xe0`\x96\\\xd8h\xbe\xc1\xa7\xf1;\xccsa\xa2\xfb\x06\x9f\xc4\xef0"n\x06\te\xcd\x86\x8b\xec\x1a\x7f\x13\xbc\xc76\x1a/\xb0i\xfcN\xf3\x02&\xe0`\x96\\\xd8h\xbe\xc1\xa7\xf1;\xccsa\xa2\xfb\x06\x9f\xc4\xef0"n\x06\te\xcd\x86\x8b\xec\x1a\x7f\x13\xbc\xc76\x1a/\xb0i\xfcN\xf3\x02&\xe0`\x96\\\xd8h\xbe\xc1\xa7\xf1;\xccsa\xa2\xfb\x06\x9f\xc4\xef0=\xb6_T\xea\xcd\x01d\x95\xcb\x97%21W\xdd\xf5\x7fcj,\xed6\xca;=\x0cT6\xe8[\x05,YFF\xdc\xe18\xf1\xf6\xa9x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xff\xd9')),
                ('pri_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homes', to='api.log_in')),
            ],
        ),
    ]
