[array] $file = Get-Content input

$array_left = [System.Collections.ArrayList]::new()
$array_right = [System.Collections.ArrayList]::new()

foreach ($line in $file) {
    $items = $line.Split(" ")
    $num_left = $items[0]
    $num_right = $items[3]
    #$num_left
    #$num_right
    [void]$array_left.Add([int]$num_left)
    [void]$array_right.Add([int]$num_right)
}
$array_left = $array_left | Sort-Object
$array_right = $array_right | Sort-Object
$array_left[0]
$array_right[0]

for ($i = 0; $i < $array_left.


