function setProgress(barId) {
    console.log("progress_"+barId);
    const progress = document.getElementById("progress_"+barId);

    value = progress.getAttribute('value')
    if (progress) {
        let set_value = 0;
        if (value < 1) {
            set_value = 0;
            time_left = "0 days"
        }
        if (value == 1) {
            set_value = 1;
            time_left = "1 day"
        }
        if (value == 2) {
            set_value = 2;
            time_left = "2 days"
        }
        if (value == 3) {
            set_value = 3;
            time_left = "3 days"
        }
        if (value == 4) {
            set_value = 4;
            time_left = "4 days"
        }
        if (value == 5) {
            set_value = 5;
            time_left = "5 days"
        }
        if (value == 6) {
            set_value = 6;
            time_left = "6 days"
        }
        if (value >= 7 && value < 14) {
            set_value = 7;
            time_left = "1 week"
        }
        if (value >= 14 && value < 21) {
            set_value = 8;
            time_left = "2 weeks"
        }
        if (value >= 21 && value < 28) {
            set_value = 9;
            time_left = "3 weeks"
        }
        if (value >= 28 && value < 30) {
            set_value = 10;
            time_left = "4 weeks"
        }
        if (value >= 30 && value < 60) {
            set_value = 11;
            time_left = "1 month"
        }
        if (value >= 60 && value < 90) {
            set_value = 12;
            time_left = "2 months"
        }
        if (value >= 90 && value < 120) {
            set_value = 13;
            time_left = "3 months"
        }
        if (value >= 120 && value < 150) {
            set_value = 14;
            time_left = "4 months"
        }
        if (value >= 150 && value < 180) {
            set_value = 15;
            time_left = "5 months"
        }
        if (value >= 180) {
            set_value = 16;
            time_left = "6+ months"
        }


        // progress.setAttribute('value', set_value/16);
        progress.style.setProperty('--progress-value', set_value/16);
    }
}

       

function setProgressText(barId, text) {
    const progress = document.getElementById(barId);
    if (progress) {
        progress.setAttribute('data-text', text);
    }
}

// Example usage:
// setProgress('progress1', 50);
// setProgressText('progress1', '50% Complete');

// setProgress('progress2', 75);
// setProgressText('progress2', 'Almost There');

function get_progress() {
    var progress = document.getElementById("progress");
    let url = '/api/'
    if (type) {
        url += '?user_id=' + type;
    }
}

