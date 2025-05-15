[app]

# Configuración básica
title = HolaMundo
package.name = holamundo
package.domain = com.ejemplo
version = 0.1  # Obligatorio
source.dir = .
source.include_exts = py,png,jpg,kv,ttf

# Dependencias
requirements = python3, kivy

# Permisos de Android
android.permissions = INTERNET

# Aceptar licencias automáticamente
android.accept_sdk_license = True

# Versiones críticas (evitan errores de SDK)
android.sdk = 34
android.ndk = 25b
android.sdk_build_tools = 34.0.0  # Versión estable

# Configuración de Python para Android
p4a.branch = develop

# Log detallado
log_level = 2