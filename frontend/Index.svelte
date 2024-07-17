<!--
Banner - A Gradio Custom Component
Created by Daniel Ialcin Misser Westergaard
https://huggingface.co/dwancin
https://github.com/dwancin
(c) 2024
-->

<svelte:options accessors={true} />

<script lang="ts">
    import type { Gradio } from "@gradio/utils";
    import { type FileData } from "@gradio/client";
    import { BlockTitle, Block } from "@gradio/atoms";
    import { StatusTracker } from "@gradio/statustracker";
    import type { LoadingStatus } from "@gradio/statustracker";
    import { tick } from "svelte";
    import MarkdownIt from 'markdown-it';
    
    // Component props
    export let gradio: Gradio<{
        change: never;
        submit: never;
        input: never;
        clear_status: LoadingStatus;
    }>;

    // Properties for the Banner component
    export let label = "";
    export let elem_id = "";
    export let elem_classes: string[] = [];
    export let visible = true;
    export let value = "";
    export let show_label: boolean;
    export let scale: number | null = null;
    export let min_width: number | undefined = undefined;
    export let loading_status: LoadingStatus | undefined = undefined;
    export let value_is_output = false;
    export let rtl = false;
    export let variant = "info";
    export let icon: FileData | null = null;
    export let size: "sm" | "lg" = "lg";
    export let show_close_button = false;
    export let show_icon = true;

    // Markdown renderer instance
    const md = new MarkdownIt();

    // Styles for different banner variants
    const VARIANT_STYLES = {
        info: {
            background: 'var(--panel-background-fill)',
            borderColor: 'var(--border-color-primary)',
            textColor: 'var(--body-text-color)',
            iconColor: 'var(--body-text-color)'
        },
        warning: {
            background: 'var(--color-yellow-50)',
            borderColor: 'var(--color-yellow-700)',
            textColor: 'var(--color-yellow-700)',
            iconColor: 'var(--color-yellow-700)'
        },
        error: {
            background: 'var(--error-background-fill)',
            borderColor: 'var(--error-border-color)',
            textColor: 'var(--error-text-color)',
            iconColor: 'var(--error-icon-color)'
        },
        success: {
            background: 'var(--color-green-50)',
            borderColor: 'var(--color-green-700)',
            textColor: 'var(--color-green-700)',
            iconColor: 'var(--color-green-700)'
        }
    };

    // Default icons for each variant
    const DEFAULT_ICONS = {
        info: `
            <svg class="info-icon" fill="none" stroke="${VARIANT_STYLES.info.iconColor}" viewBox="0 0 24 24" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z"></path>
            </svg>
        `,
        warning: `
            <svg class="warning-icon" fill="none" stroke="${VARIANT_STYLES.warning.iconColor}" stroke-width="2" viewBox="0 0 24 24" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"></path>
            </svg>
        `,
        error: `
            <svg class="error-icon" fill="none" stroke="${VARIANT_STYLES.error.iconColor}" viewBox="0 0 24 24" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z"></path>
            </svg>
        `,
        success: `
            <svg class="success-icon" fill="none" stroke="${VARIANT_STYLES.success.iconColor}" viewBox="0 0 24 24" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2l4-4m5.455 2.455A9 9 0 1 1 12 3a9 9 0 0 1 8.455 8.455z"></path>
            </svg>
        `
    };

    // Handler for the change event
    function handle_change(): void {
        gradio.dispatch("change");
        if (!value_is_output) {
            gradio.dispatch("input");
        }
    }

    // Handler for the close button click event
    function handle_close(): void {
        visible = false;
        gradio.dispatch("change");
    }

    // Reactive statements for updating value and label content
    $: if (value === null) value = "";
    $: value, handle_change();

    // Default labels based on variant
    const DEFAULT_LABELS = {
        info: "Info",
        warning: "Warning",
        error: "Error",
        success: "Success"
    };

    // Use default label if none is provided
    $: if (!label) {
        label = DEFAULT_LABELS[variant];
    }

    // Rendered markdown content
    $: renderedValueContent = md.render(value);
    $: renderedLabelContent = md.render(label);
</script>

<Block
    {visible}
    {elem_id}
    {elem_classes}
    {scale}
    {icon}
    {size}
    {min_width}
    allow_overflow={true}
    container={false}
    padding={true}
    class={`banner ${size}`}
>
    <StatusTracker
        autoscroll={gradio.autoscroll}
        i18n={gradio.i18n}
        {...loading_status}
        variant="center"
        on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
    />
    
    <div class:pending={loading_status?.status === "pending"}>
        {#if size === "sm"}
            <div
                class="small-banner"
                style={`
                    display: flex;
                    align-items: center;
                    width: 100%;
                    border-radius: var(--block-radius);
                    padding: var(--spacing-md) var(--spacing-xxl);
                    border: var(--input-border-width) solid;
                    background: ${VARIANT_STYLES[variant].background};
                    color: ${VARIANT_STYLES[variant].borderColor};
                    column-gap: var(--spacing-lg);
                    cursor: default;
                `}
            >
                {#if show_icon}
                    <div class="icon-sm">
                        {#if icon}
                            <img src={icon} style={`color: ${VARIANT_STYLES[variant].iconColor};`} />
                        {:else}
                            {@html DEFAULT_ICONS[variant]}
                        {/if}
                    </div>
                {/if}
                <div class="text-sm">
                    {#if show_label}
                        <div class="label-sm" style={`color: ${VARIANT_STYLES[variant].textColor};`}>{@html renderedLabelContent}</div>
                    {/if}
                    <div class="value-sm" style={`color: ${VARIANT_STYLES[variant].textColor};`}>{@html renderedValueContent}</div>
                </div>
                {#if show_close_button}
                    <button class="button" id="buttonSmall" title="Hide" on:click={handle_close} style={`color: ${VARIANT_STYLES[variant].textColor};`}>&times;</button>
                {/if}
            </div>
        {:else}
            <div
                class="large-banner"
                style={`
                    display: flex;
                    align-items: center;
                    width: 100%;
                    border-radius: var(--block-radius);
                    padding: var(--spacing-xxl);
                    border: var(--input-border-width) solid;
                    background: ${VARIANT_STYLES[variant].background};
                    color: ${VARIANT_STYLES[variant].borderColor};
                    column-gap: var(--spacing-lg);
                    cursor: default;
                `}
            >
                {#if show_icon}
                    <div class="icon-lg">
                        {#if icon}
                            <img src={icon} style={`color: ${VARIANT_STYLES[variant].iconColor};`} />
                        {:else}
                            {@html DEFAULT_ICONS[variant]}
                        {/if}
                    </div>
                {/if}
                <div class="text-lg">
                    {#if show_label}
                        <div class="label-lg" style={`color: ${VARIANT_STYLES[variant].textColor};`}>{@html renderedLabelContent}</div>
                    {/if}
                    <div class="value-lg" style={`color: ${VARIANT_STYLES[variant].textColor};`}>{@html renderedValueContent}</div>
                </div>
                {#if show_close_button}
                    <button class="button" id="buttonLarge" title="Hide" on:click={handle_close} style={`color: ${VARIANT_STYLES[variant].textColor};`}>&times;</button>
                {/if}
            </div>
        {/if}
    </div>
</Block>

<style>
    div {
        transition: 150ms;
    }
    
    .icon-lg {
        max-width: var(--size-9);
        opacity: 0.8;
    }
    
    .icon-sm {
        max-width: var(--size-5);
        opacity: 0.8;
    }

    .text-lg {
        display: flex;
        flex-direction: column;
    }
    
    .text-sm {
        display: flex;
        justify-content: flex-start;
        gap: var(--spacing-sm);
    }

    .value-lg {
        font-size: var(--size-4);
    }
    
    .text-sm {
        display: flex;
        justify-content: flex-start;
        gap: var(--spacing-sm);
        align-items: center;
    }

    .label-lg {
        font-size: var(--size-5);
        font-weight: var(--prose-header-text-weight);
    }
    
    .label-sm {
        font-size: var(--size-4);
        font-weight: var(--prose-header-text-weight);
    }
    
    .button {
        position: absolute;
        top: 0;
        bottom: 0;
        opacity: 0.5;
    }
    
    .button:hover {
        opacity: 1;
    }
    
    #buttonLarge {
        right: 30px;
        font-size: var(--size-6) !important;
    }
    
    #buttonSmall {
        right: 13px;
        font-size: var(--size-5) !important;
    }
</style>
