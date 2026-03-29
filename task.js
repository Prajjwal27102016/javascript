< !DOCTYPE html >
    <html lang="en">
        <head>
            <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Subject Marks Calculator</title>
                    <style>
                        body {font - family: sans-serif; display: flex; justify-content: center; padding: 50px; }
                        .card {border: 1px solid #ddd; padding: 20px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
                        input {display: block; margin: 10px 0; padding: 8px; width: 200px; }
                        button {background - color: #007bff; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; }
                        button:hover {background - color: #0056b3; }
                        #result {margin - top: 20px; font-weight: bold; font-size: 1.2em; color: #28a745; }
                    </style>
                </head>
                <body>

                    <div class="card">
                        <h2>Marks Calculator</h2>
                        <label>Subject 1:</label>
                        <input type="number" id="m1" placeholder="Enter marks">

                            <label>Subject 2:</label>
                            <input type="number" id="m2" placeholder="Enter marks">

                                <label>Subject 3:</label>
                                <input type="number" id="m3" placeholder="Enter marks">

                                    <button onclick="calculateSum()">Calculate Total</button>

                                    <div id="result"></div>
                                </div>

                                <script>
                                    function calculateSum() {
        // Get values from inputs and convert to numbers
        const mark1 = parseFloat(document.getElementById('m1').value) || 0;
                                    const mark2 = parseFloat(document.getElementById('m2').value) || 0;
                                    const mark3 = parseFloat(document.getElementById('m3').value) || 0;

                                    // Calculate sum
                                    const total = mark1 + mark2 + mark3;

                                    // Display the result
                                    document.getElementById('result').innerText = "Total Sum: " + total;
    }
                                </script>

                            </body>
                        </html>
