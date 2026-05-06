const predictBtn = document.getElementById("predictBtn");

predictBtn.addEventListener("click", async () => {

    // INPUT VALUES

    const material =
        document.getElementById("material").value;

    const capacitance =
        document.getElementById("capacitance").value;

    const voltage =
        document.getElementById("voltage").value;

    const currentDensity =
        document.getElementById("currentDensity").value;

    const surfaceArea =
        document.getElementById("surfaceArea").value;

    // LOADING EFFECT

    document.getElementById("efficiency").innerText =
        "Loading...";

    document.getElementById("energy").innerText =
        "...";

    document.getElementById("power").innerText =
        "...";

    document.getElementById("cycle").innerText =
        "...";

    try {

        // SEND TO BACKEND

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    material,
                    capacitance,
                    voltage,
                    currentDensity,
                    surfaceArea
                })
            }
        );

        const data = await response.json();

        // UPDATE UI WITH REAL RESULTS

        document.getElementById("efficiency").innerText =
            data.efficiency;

        document.getElementById("energy").innerText =
            data.energy_density;

        document.getElementById("power").innerText =
            data.power_density;

        document.getElementById("cycle").innerText =
            data.cycle_stability;

    } catch (error) {

        console.log(error);

        alert("Prediction failed");
    }
});