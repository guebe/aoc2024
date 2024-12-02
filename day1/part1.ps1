$list1 = [System.Collections.ArrayList]::new()
$list2 = [System.Collections.ArrayList]::new()

foreach ($line in Get-Content input) {
    $items = $line.Split(" ")
    [void]$list1.Add([int] $items[0])
    [void]$list2.Add([int] $items[3])
}

$list1 = $list1 | Sort-Object
$list2 = $list2 | Sort-Object

$sum = 0
for ($i = 0; $i -lt $list1.Count; $i++) {
    $sum += [Math]::Abs($list1[$i] - $list2[$i])
}
$sum
