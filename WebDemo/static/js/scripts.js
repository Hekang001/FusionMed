function adjustHeight(element) {
    element.style.height = "auto"; // 重置高度
    element.style.height = (element.scrollHeight) + "px"; // 重新设置为内容高度
}

// 页面加载完成后自动调整输出框的高度
document.addEventListener("DOMContentLoaded", function() {
    var outputText = document.getElementById("output_text");
    if (outputText) {
        adjustHeight(outputText);
    }
});