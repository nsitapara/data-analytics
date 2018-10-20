
'This method only works if the data is sorted. if not sorted, can add in a command to sort before the loops.

Sub EasyMethod()

' need 3 counters/place holders. 1)total volume for ticker 2)counter to track position for the final table 3)number of rows to store the endpoint for the loop, make it dynamic in range
Range("K:L").Clear

'for loop, goes through first column to test if the value of row below is the same value, if so add to total. else add to total, write the values
'important to zero out total and add 1 to position counter

For Each ws In Worksheets

Dim total, position, numberOfRows As Double
numberOfRows = ws.Cells(1, 1).End(xlDown).Row
position = 2
ws.Range("K1") = "Ticker"
ws.Range("L1") = "Total count"

    For rowplace = 2 To numberOfRows

        If ws.Cells(rowplace + 1, 1) = ws.Cells(rowplace, 1) Then
            total = total + ws.Cells(rowplace, 7).Value
        Else
            total = total + ws.Cells(rowplace, 7).Value
            ws.Range("K" & position) = ws.Cells(rowplace, 1)
            ws.Range("L" & position) = total
            position = position + 1
            total = 0
        End If

    Next rowplace
Next ws


End Sub
