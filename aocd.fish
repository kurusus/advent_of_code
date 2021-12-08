function aocd
    set run_dir $HOME/advent_of_code/run
    mkdir $run_dir
    cp $argv $run_dir/run.py
    cp $HOME/advent_of_code/aocd.py $run_dir
    python $run_dir/run.py
    rm -rf $run_dir
end
