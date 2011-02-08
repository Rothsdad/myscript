;;========================================
;; 路径设置
;;========================================

;;我的load-path
 (add-to-list 'load-path "~/elisp/")

;;========================================
;; 外观设置
;;========================================

;;禁用工具栏
(tool-bar-mode nil)

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

;;========================================
;; load w3m
;;========================================

(require 'w3m-load)

;;========================================
;; 显示行号
;;========================================

(require 'linum)
(global-linum-mode t)

;;========================================
;; 设置字体
;;========================================

(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 )
(custom-set-faces
  ;; custom-set-faces was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :background "black" :foreground "#c0c0c0" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 120 :width normal :foundry "unknown" :family "DejaVu Sans Mono")))))
