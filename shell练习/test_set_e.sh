set -e
i=1
while (( $i<3 ))
do 
    sleep 1
    echo "good"
    i++
    echo $?
done

echo "666"
