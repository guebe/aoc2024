[array] $file = Get-Content input
$list1 = [System.Collections.ArrayList]::new()
$list2 = [System.Collections.ArrayList]::new()

foreach ($line in $file) {
    $items = $line.Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)
    [void]$list1.Add([int] $items[0])
    [void]$list2.Add([int] $items[1])
}

$list1 = $list1 | Sort-Object
$list2 = $list2 | Sort-Object

$sum = 0
for ($i = 0; $i -lt $list1.Count; $i++) {
    $num1 = $list1[$i]
    
    $count = 0
    foreach ($num2 in $list2) {
        if ($num1 -eq $num2) {
            $count++
        }
    }

    $sum = $sum + $count * $num1
}

$sum

