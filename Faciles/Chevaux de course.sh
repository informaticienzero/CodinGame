read N
for (( i=0; i<N; i++ )); do
    read Pi
    powers[i]=$Pi
done

sorted_powers=( $( printf "%s\n" "${powers[@]}" | sort -n ) )
shortest_difference=545554

for (( i=0; i<N; i++ )); do
    if [ i != 0 ]
    then
        previous=${sorted_powers[i-1]}
        current=${sorted_powers[i]}
            
        if [ $current -lt $previous ]
        then
            difference=$previous-$current
        else
            difference=$current-$previous 
        fi
            
        if [[ $difference -lt $shortest_difference ]]
        then
            shortest_difference=$difference
        fi
    fi
done

echo $shortest_difference | bc
