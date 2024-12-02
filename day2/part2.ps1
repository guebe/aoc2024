function check_line {

    param (
        $items
    )

    $num1 = [int]$items[0]
    $items = $items[1..$items.Count]
    $dir = 0

    for ($i = 0; $i -lt $items.Count; $i++) {
        $num2 = [int]$items[$i]
        if ($num2 -gt $num1) {
            $diff = $num2 - $num1
            if (($dir -eq -1) -or ($diff -gt 3)) {
		return $i + 1
            }
            $dir = 1
        }
        elseif ($num2 -lt $num1) {
            $diff = $num1 - $num2
            if (($dir -eq 1) -or ($diff -gt 3)) {
		return $i + 1
            }
            $dir = -1
        }
        else {
	    return $i + 1
        }
        $num1 = $num2
    }
    return -1
}

[array] $file = Get-Content input
$list1 = [System.Collections.ArrayList]::new()
$list2 = [System.Collections.ArrayList]::new()

$sum = 0

foreach ($line in $file) {
    $items = $line.Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)
    $i = check_line $items
    $i2 = check_line $items[1..$items.Count]
    $i3 = check_line $items[0..($items.Count-1)]
    $safe = 1
    if ($i -ne -1 -and $i2 -ne -1 -and $i3 -ne -1) {
       $t1 = $items[0..($i-1)] + $items[($i+1)..$items.Count]
       $t2 = $items[0..($i-2)] + $items[($i)..$items.Count]
       $i = check_line $t1
       $i2 = check_line $t2
       if ($i -ne -1 -and $i2 -ne -1) {
           $safe = 0
	   #$i
           #$items -join " "
           #$t1 -join " "
           #$t2 -join " "
       }
    }
    #$safe
    $sum = $sum + $safe
}

$sum

