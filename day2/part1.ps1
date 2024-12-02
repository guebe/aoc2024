
[array] $file = Get-Content input
$list1 = [System.Collections.ArrayList]::new()
$list2 = [System.Collections.ArrayList]::new()

$sum = 0

foreach ($line in $file) {
    $items = $line.Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)

    $num1 = [int]$items[0]
    $items = $items[1..$items.Count]
    #$num1
    #"***"
    #$items
    $dir = 0
    $safe = 1

    foreach ($num2 in $items) {
        $num2 = [int]$num2
	$diff = [Math]::Abs($num2 - $num1)
	if ($diff -lt 1 -or $diff -gt 3) {
	    $safe = 0
	    break
	}
        if ($num2 -gt $num1) {
            if ($dir -eq -1) {
                $safe = 0
                break
            }
            $dir = 1
        }
        elseif ($num2 -lt $num1) {
            if ($dir -eq 1) {
                $safe = 0
                break
            }
            $dir = -1
        }
        $num1 = $num2
    }
    #$safe
    $sum = $sum + $safe
}

$sum

