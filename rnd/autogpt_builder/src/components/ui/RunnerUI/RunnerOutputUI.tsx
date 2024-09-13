import React from "react";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetDescription,
} from "@/components/ui/sheet";
import { ScrollArea } from "@/components/ui/scroll-area";
import { BlockIORootSchema } from "@/lib/autogpt-server-api/types";

interface BlockOutput {
  id: string;
  outputSchema: BlockIORootSchema;
  hardcodedValues: {
    name: string;
    description: string;
  };
  result?: any;
}

interface OutputModalProps {
  isOpen: boolean;
  onClose: () => void;
  blockOutputs: BlockOutput[];
}

const formatOutput = (output: any): string => {
  if (typeof output === "object") {
    return JSON.stringify(output, null, 2);
  }
  return String(output);
};

export function RunnerOutputUI({
  isOpen,
  onClose,
  blockOutputs,
}: OutputModalProps) {
  return (
    <Sheet open={isOpen} onOpenChange={onClose}>
      <SheetContent
        side="right"
        className="flex h-full w-full flex-col overflow-hidden sm:max-w-[500px]"
      >
        <SheetHeader className="px-2 py-2">
          <SheetTitle className="text-xl">Run Outputs</SheetTitle>
          <SheetDescription className="mt-1 text-sm">
            View the outputs from your agent run.
          </SheetDescription>
        </SheetHeader>
        <div className="flex-grow overflow-y-auto px-2 py-2">
          <ScrollArea className="h-full overflow-auto pr-4">
            <div className="space-y-4">
              {blockOutputs && blockOutputs.length > 0 ? (
                blockOutputs.map((block) => (
                  <div key={block.id} className="space-y-1">
                    <h3 className="text-base font-semibold">
                      {block.hardcodedValues.name || "Unnamed Output"}
                    </h3>

                    {block.hardcodedValues.description && (
                      <p className="text-sm text-gray-600">
                        {block.hardcodedValues.description}
                      </p>
                    )}

                    <div className="rounded-md bg-gray-100 p-2">
                      <pre className="whitespace-pre-wrap break-words text-sm">
                        {formatOutput(block.result ?? "No output yet")}
                      </pre>
                    </div>
                  </div>
                ))
              ) : (
                <p>No output blocks available.</p>
              )}
            </div>
          </ScrollArea>
        </div>
      </SheetContent>
    </Sheet>
  );
}

export default RunnerOutputUI;