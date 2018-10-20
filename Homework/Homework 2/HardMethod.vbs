
'This method only works if the data is sorted. if not sorted, can add in a command to sort before the loops.

Sub HardMethod()

' need 3 counters/place holders. 1)total volume for ticker 2)counter to track position for the final table 3)number of rows to store the endpoint for the loop, make it dynamic in range
Range("K:L").Clear

'for loop, goes through first column in each WORKSHEET to test if the value of row below is the same value, if so add to total. else add to total, write the values
'important to zero out total and add 1 to position counter

For Each ws In Worksheets

'clearfunction
ws.Range("H:V").Clear

'add variable for program
Dim total, position, numberOfRows, CloseValue, OpenValue, YearlyChange, PercentChange As Double

Dim switch As Integer

'use this variable to figure out the number or rows in the sheet, this serves as the end point for the FOR loop
numberOfRows = ws.Cells(1, 1).End(xlDown).Row
position = 2

'adding titles
ws.Range("K1") = "Ticker"
ws.Range("L1") = "Total count"
ws.Range("M1") = "Yearly Change"
ws.Range("N1") = "Percent Change"
ws.Range("Q2") = "Greatest % Increase"
ws.Range("Q3") = "Greatest % Decrease"
ws.Range("Q4") = "Greatest Total Volume"
ws.Range("S1") = "Ticker"
ws.Range("T1") = "Value"

'using a switch to keep track of open option, which is only ran on the first value element of the same ticker value, onces triggered the value is changed to 0
switch = 1
    For rowplace = 2 To numberOfRows
'if conditional to test for the value below is the same
        If (ws.Cells(rowplace + 1, 1) = ws.Cells(rowplace, 1)) Then
            total = total + ws.Cells(rowplace, 7).Value
            'used to keep track of the first element in the same ticker
            If switch = 1 Then
                OpenValue = ws.Cells(rowplace, 3).Value
                switch = 0
            End If
            'write out the information and 0 out the total and reset switch and add 1 to position value for the summary table

        Else
            total = total + ws.Cells(rowplace, 7).Value
            ws.Range("K" & position) = ws.Cells(rowplace, 1)
            ws.Range("L" & position) = total
            CloseValue = ws.Cells(rowplace, 6)
            If OpenValue <> 0 Then
                YearlyChange = (CloseValue - OpenValue)
                PercentChange = YearlyChange / OpenValue
                ws.Range("M" & position) = YearlyChange
                ws.Range("N" & position) = PercentChange
            End If
            
            position = position + 1
            total = 0
            switch = 1
        End If
    Next rowplace
    
'Loop for formating the cells to green(>0) and red(<0)
numberOfRows = ws.Cells(1, 13).End(xlDown).Row

    For rowplace = 2 To numberOfRows

    If ws.Cells(rowplace, 13).Value > 0 Then

        ws.Cells(rowplace, 13).Interior.ColorIndex = 4
    Else

        ws.Cells(rowplace, 13).Interior.ColorIndex = 3

    End If
numberOfRows = ws.Cells(1, 11).End(xlDown).Row


    Next rowplace

'apply style Percent to N, dependent on numberOfRows value in the expression above
ws.Range("N2:N" & numberOfRows).Style = "Percent"

Dim GIncrease, GDecrease, GTVolume As Double
Dim GIncreaseName, GDecreaseName, GTVolumeName As String

'for loop goes though the data to find the highest, lowest and volume by updaing the value if the value is higher/lower 
For rowplace = 2 To numberOfRows

    If ws.Cells(rowplace, 14) > GIncrease Then

        GIncrease = ws.Cells(rowplace, 14)
        GIncreaseName = ws.Cells(rowplace, 11)
    End If


    If ws.Cells(rowplace, 14) < GDecrease Then

        GDecrease = ws.Cells(rowplace, 14)
        GDecreaseName = ws.Cells(rowplace, 11)

    End If

    If ws.Cells(rowplace, 12) > GTVolume Then
        GTVolume = ws.Cells(rowplace, 12)
        GTVolumeName = ws.Cells(rowplace, 11)
    End If

Next rowplace


'writes out the found values for the increase,decrease,volume and the tickers for the items
ws.Range("T2") = GIncrease
ws.Range("T3") = GDecrease
ws.Range("T4") = GTVolume
ws.Range("S2") = GIncreaseName
ws.Range("S3") = GDecreaseName
ws.Range("S4") = GTVolumeName

'this applies the style percent to the cells T2 and T3

ws.Range("T2:T3").Style = "Percent"


Next ws


End Sub

