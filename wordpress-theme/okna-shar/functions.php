<?php
/**
 * EVO — ОКНА Ш.А.Р. block theme setup.
 */

if (!defined('ABSPATH')) {
    exit;
}

add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style(
        'evo-okna-shar',
        get_stylesheet_uri(),
        [],
        wp_get_theme()->get('Version')
    );
});

add_action('after_setup_theme', function () {
    add_theme_support('editor-styles');
    add_editor_style('style.css');
});
