#!/bin/bash

if [ -n "$1" ]
then
  python manage.py test --settings=torpedo.dev_settings $*
else
  python manage.py $*
fi

