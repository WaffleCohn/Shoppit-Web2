var step = 1,
    numSteps = 4;

function nextt(obj)
{
    if (obj.className.indexOf("disabled") == -1)
    {
        step++;

        if (step <= numSteps)
        {
            var currentStep = document.getElementById("step" + (step-1)),
                nextStep = document.getElementById("step" + step);

            currentStep.style.display = "none";
            nextStep.style.display = "block";

            var previousButton = document.getElementById("previous"),
                submitButton = document.getElementById("submit-button");

            previousButton.className = "nav-button";
            submitButton.style.display = "none";
        }

        if (step > numSteps-1)
        {
            var nextButton = document.getElementById("next"),
                submitButton = document.getElementById("submit-button");

            nextButton.className += " disabled";

            submitButton.style.display = "block";
        }
    }
}

function previous(obj)
{
    if (obj.className.indexOf("disabled") == -1)
    {
        step--;

        if (step > 0)
        {
            var currentStep = document.getElementById("step" + (step+1)),
                prevStep = document.getElementById("step" + step);

            currentStep.style.display = "none";
            prevStep.style.display = "block";

            var nextButton = document.getElementById("next"),
                submitButton = document.getElementById("submit-button");

            nextButton.className = "nav-button";
            submitButton.style.display = "none";
        }

        if (step <= 1)
        {
            var prevButton = document.getElementById("previous");
            prevButton.className += " disabled";
        }
    }
}
