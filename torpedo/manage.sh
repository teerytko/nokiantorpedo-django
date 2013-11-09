#!/bin/bash

if [ -n "$1" ]
then
  python manage.py $* --settings=torpedo.prod_settings
else
  python manage.py $*
fi

