# ibus
export XMODIFIERS=@im=ibus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
ibus-daemon -d -x

# swap CapsLock and Ctrl
xmodmap ~/.xmodmap

