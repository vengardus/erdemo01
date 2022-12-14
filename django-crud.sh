#django-crud %model%
#created by vengardus; generated by alice
DIR_TEMPLATES='/media/vengardus/e386a30c-7012-4df6-90c8-9fe86a3ae459/vengardus/projects/django/alice/templates'
DIR_PROJECT='/media/vengardus/e386a30c-7012-4df6-90c8-9fe86a3ae459/vengardus/projects/django/erdemo01'
DIR_APP='base'

if [[ $# != 1 ]];then
	echo 'Error sintaxis: django-crud model_name' && exit 1
fi

PARM=$1 && MODEL_CAPITALIZE=${PARM^} && MODEL_LOWER=${PARM,,}

echo "Creando b${MODEL_LOWER}.py"
cp  $DIR_TEMPLATES/bmodel.py $DIR_PROJECT/$DIR_APP/business/b$MODEL_LOWER.py
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/$DIR_APP/business/b$MODEL_LOWER.py
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/$DIR_APP/business/b$MODEL_LOWER.py
sed -i "s,__date__,$(date),g" $DIR_PROJECT/$DIR_APP/business/b$MODEL_LOWER.py

echo "Creando ${MODEL_LOWER}_view.py"
cp  $DIR_TEMPLATES/model_view.py $DIR_PROJECT/$DIR_APP/views/"$MODEL_LOWER"_view.py
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/$DIR_APP/views/"$MODEL_LOWER"_view.py
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/$DIR_APP/views/"$MODEL_LOWER"_view.py
sed -i "s,__date__,$(date),g" $DIR_PROJECT/$DIR_APP/views/"$MODEL_LOWER"_view.py

echo "Creando ${MODEL_LOWER}_api.py"
cp  $DIR_TEMPLATES/model_api.py $DIR_PROJECT/$DIR_APP/api/"$MODEL_LOWER"_api.py
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/$DIR_APP/api/"$MODEL_LOWER"_api.py
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/$DIR_APP/api/"$MODEL_LOWER"_api.py
sed -i "s,__date__,$(date),g" $DIR_PROJECT/$DIR_APP/api/"$MODEL_LOWER"_api.py

echo "Creando ${MODEL_LOWER}_form.py"
cp  $DIR_TEMPLATES/model_form.py $DIR_PROJECT/$DIR_APP/forms/"$MODEL_LOWER"_form.py
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/$DIR_APP/forms/"$MODEL_LOWER"_form.py
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/$DIR_APP/forms/"$MODEL_LOWER"_form.py
sed -i "s,__date__,$(date),g" $DIR_PROJECT/$DIR_APP/forms/"$MODEL_LOWER"_form.py

echo "Creando ${MODEL_LOWER}_list.html"
_DIR="$DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER"
[ ! -d $_DIR ] && mkdir $_DIR
cp  $DIR_TEMPLATES/model_list.html $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_list.html
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_list.html
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_list.html
sed -i "s,__date__,$(date),g" $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_list.html

echo "Creando ${MODEL_LOWER}_form.html"
cp  $DIR_TEMPLATES/model_form.html $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_form.html
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_form.html
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_form.html
sed -i "s,__date__,$(date),g" $DIR_PROJECT/$DIR_APP/templates/base/$MODEL_LOWER/"$MODEL_LOWER"_form.html

echo "Creando ${MODEL_LOWER}_list.js"
_DIR="$DIR_PROJECT/static/js/$MODEL_LOWER"
[ ! -d $_DIR ] && mkdir $_DIR
cp  $DIR_TEMPLATES/model_list.js $DIR_PROJECT/static/js/$MODEL_LOWER/"$MODEL_LOWER"_list.js
sed -i "s/__model__/${MODEL_LOWER}/g" $DIR_PROJECT/static/js/$MODEL_LOWER/"$MODEL_LOWER"_list.js
sed -i "s,__Model__,$MODEL_CAPITALIZE,g" $DIR_PROJECT/static/js/$MODEL_LOWER/"$MODEL_LOWER"_list.js
sed -i "s,__date__,$(date),g" $DIR_PROJECT/static/js/$MODEL_LOWER/"$MODEL_LOWER"_list.js