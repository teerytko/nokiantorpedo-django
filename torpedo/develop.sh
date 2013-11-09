#!/bin/bash

if [ -n "$1" ]
then
  python manage.py $* --settings=torpedo.proddev_settings
else
  python manage.py $*
fi

