/*----------------------日期計算----------------------*/ 
function calculateDateDiff(startDate, endDate) {
    // 轉換成 Date
    const start = new Date(startDate);
    const end = new Date(endDate);

    // 計算年、月、天
    let years = end.getFullYear() - start.getFullYear();
    let months = end.getMonth() - start.getMonth();
    let days = end.getDate() - start.getDate();

    // 如果天數為負數，借一个月
    if (days < 0) {
        months -= 1;
        const prevMonth = new Date(end.getFullYear(), end.getMonth(), 0); // 获取上个月的最后一天
        days += prevMonth.getDate();
    }

    // 如果月份為負數，借一年
    if (months < 0) {
        years -= 1;
        months += 12;
    }

    return { years, months, days };
}

// 輸入數據
const birthDate = "2023-08-25";
const today = new Date().toISOString().split("T")[0]; // 当前日期
const homeDate = "2024-09-27";

// 計算日数
const birthDiff = calculateDateDiff(birthDate, today);
const homeDiff = calculateDateDiff(homeDate, today);

// 更新 HTML 内容
document.getElementById("birthDays").textContent = `${birthDiff.years}年 ${birthDiff.months}個月 ${birthDiff.days}天`;
document.getElementById("homeDays").textContent = `${homeDiff.years}年 ${homeDiff.months}個月 ${homeDiff.days}天`;

/*----------------------新增、修改按鈕----------------------*/ 
function bindEventButtons() {

    $('.addBtn').off('click').on('click', function() {
        const date = $(this).attr('id');
        $('#eventForm').show();
        $('#eventDataForm').off('submit').on('submit', function(e) {
            e.preventDefault();
            submitFormData(date, 'POST');
        });
    });

    $('.updateBtn').off('click').on('click', function() {
        const date = $(this).attr('id');
        $('#eventForm').show();
        $('#eventDataForm').off('submit').on('submit', function(e) {
            e.preventDefault();
            submitFormData(date, 'PUT');
        });
    });
}

function submitFormData(date, method) {
    const data = JSON.stringify({
        mental: $('#mental').val(),
        weight: $('#weight').val(),
        video: $('#video').val(),
    });

    $.ajax({
        url: `/daily_log_manage/${date}/`,
        method: method,
        contentType: 'application/json',
        data: data,
        success: function() {
            alert("資料已成功提交！");
            $('#eventForm').hide();
            $('#calendar').fullCalendar('refetchEvents'); // 更新日曆
        },
        error: function() {
            alert("資料提交失敗！");
        }
    });
}