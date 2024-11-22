document.addEventListener('DOMContentLoaded', function() {
    // 使用 Intersection Observer 实现表格懒加载
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        rootMargin: '50px',
        threshold: 0.1
    });

    // 观察所有表格容器
    document.querySelectorAll('.table-container').forEach(table => {
        observer.observe(table);
    });
}); 