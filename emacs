;;========================================
;; 路径设置
;;========================================

;;我的load-path
 (add-to-list 'load-path "~/elisp/")

;;========================================
;; 外观设置
;;========================================

;;禁用工具栏
;;(tool-bar-mode nil)

;;禁用菜单栏，F10 开启关闭菜单
;;(menu-bar-mode nil)

;;禁用滚动栏，用鼠标滚轮代替
(scroll-bar-mode nil)

;;禁用启动画面
(setq inhibit-startup-message t)

;;========================================
;; 颜色主题
;;========================================

;;加载color-theme
(require 'color-theme)
(eval-after-load "color-theme"
  '(progn
     (color-theme-initialize)
     (color-theme-hober)))

;;========================================
;; lua-mode
;;========================================

(setq auto-mode-alist (cons '("\.lua$" . lua-mode) auto-mode-alist))
(autoload 'lua-mode "lua-mode" "Lua editing mode." t)
